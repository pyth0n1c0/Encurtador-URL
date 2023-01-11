from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd
from secrets import token_urlsafe
from random import randint

# Cadastrar URL_encurtada no DB -> CHECK
# Retornar a URL encurtada -> CHECK
# Lógica front-end do icon de copy e ENTER=submit ->CHECK
# Construir lógica de redirecionamento das URLs
# Deploy e configurações extras
# v2.0
#	API
#	Estatísticas de URL
db = SQLAlchemy()
DB_NAME = 'storage.db'

def create_database(app):
	if not path.exists(path.abspath(DB_NAME)):
		with app.app_context():
			db.create_all()

def generate_url_code():
	# Calcular número possível de URLs
	len_url = randint(4, 6)
	random_url = token_urlsafe(len_url)
	return random_url

def create_app():
	app = Flask(__name__, static_folder='static', template_folder='templates')
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.abspath(DB_NAME)}'

	from .models import URLs

	db.init_app(app)
	create_database(app)

	@app.route('/', methods=['GET', 'POST'])
	def index():
		if request.method == 'POST':
			if request.form.get('url_original'):
				url_original = request.form.get('url_original')
				url_code = generate_url_code()
				url_encurtada = f'http://localhost/' + url_code 
				
				nova_url = URLs(url_origin=url_original, url_code=url_code)
				db.session.add(nova_url)
				db.session.commit()

				return render_template('index.html', url_encurtada=url_encurtada)
		return render_template('index.html')

	@app.route('/<url_code>')
	def redirect_url(url_code):
		url_object = URLs.query.filter_by(url_code=url_code).first()
		url = url_object.url_origin.replace('\r\n', '')

		if url[:4].lower() != 'http':
			url = 'http://' + url
		return redirect(url)

	@app.route('/url/')
	def url_detail():
		urls = URLs.query.all()
		return render_template("detail.html", urls=urls)

	return app

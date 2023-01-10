from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd
from secrets import token_urlsafe
from random import randint
# API

db = SQLAlchemy()
DB_NAME = 'storage.db'

def create_database(app):
	if not path.exists(path.abspath(DB_NAME)):
		with app.app_context():
			db.create_all()

def __generate_shortened_url():
	# Calcular número possível de URLs
	len_url = randint(4, 10)
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
				url_encurtada = __generate_shortened_url()
				
				nova_url = URLs(url_original=url_original, url_encurtada=url_encurtada)
				db.session.add(nova_url)
				db.session.commit()

				print('URL ->', url_original)
				print('URL Object ->', nova_url)

		return render_template('index.html')


	@app.route("/url/")
	def url_detail():
	    urls = URLs.query.all()
	    return render_template("detail.html", urls=urls)

	return app
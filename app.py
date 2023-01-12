from flask import Flask, render_template, request, redirect
from secrets import token_urlsafe
from random import randint

def generate_url_code():
	len_url = randint(4, 6)
	random_url = token_urlsafe(len_url)
	return random_url

def create_app(config_mode, server_mode):
	app = Flask(__name__, static_folder='static', template_folder='templates')
	app.config.from_object(config_mode)
	app.config.from_pyfile('config.py')

	from models import URLs, create_development_db, db

	db.init_app(app)
	if server_mode == 'development':
		create_development_db(app)

	@app.route('/', methods=['GET', 'POST'])
	def index():
		if request.method == 'POST':
			if request.form.get('url_original'):
				url_original = request.form.get('url_original').replace('\r\n', '')
				url_code = generate_url_code()
				url_encurtada = f'{app.config["IP_HOST"]}:{app.config["PORT_HOST"]}/{url_code}' 
				
				nova_url = URLs(url_origin=url_original, url_code=url_code)
				db.session.add(nova_url)
				db.session.commit()

				return render_template('index.html', url_encurtada=url_encurtada)
		return render_template('index.html')

	@app.route('/<url_code>')
	def redirect_url(url_code):
		url_object = URLs.query.filter_by(url_code=url_code).first()
		url = url_object.url_origin

		if url[:4].lower() != 'http':
			url = 'http://' + url
		return redirect(url)

	return app

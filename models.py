from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'storage.db'

class URLs(db.Model):
	__tablename__ = 'urls'

	id = db.Column(db.Integer, primary_key=True)
	url_origin = db.Column(db.Text)
	url_code = db.Column(db.String(100) ,unique=True)

	def __repr__(self):
		return f'<URL {self.id} {self.url_origin} {self.url_code}>'

def create_development_db(app):
	if not path.exists(path.abspath(DB_NAME)):
		with app.app_context():
			db.create_all()
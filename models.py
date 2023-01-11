from .app import db

class URLs(db.Model):
	__tablename__ = 'urls'

	id = db.Column(db.Integer, primary_key=True)
	url_original = db.Column(db.Text)
	codigo_url_encurtada = db.Column(db.String(100) ,unique=True)

	def __repr__(self):
		return f'<URL {self.id} - {self.codigo_url_encurtada}>'

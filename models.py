from .app import db

class URLs(db.Model):
	__tablename__ = 'urls'

	id = db.Column(db.Integer, primary_key=True)
	url_origin = db.Column(db.Text)
	url_code = db.Column(db.String(100) ,unique=True)

	def __repr__(self):
		return f'<URL {self.id} {self.url_origin} {self.url_code}>'

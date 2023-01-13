from os import path, environ

class Config():
	SECRET_KEY = 'd+;2:sD,HY@u]C^1[:ASg}P2[[dCP.;S4*~(>1~c^)6_q`.*xjO]z!pVtD;z#)i1+|/-8'
	ROOT_DIR = path.dirname(path.abspath(__file__))

class ConfigDevelopment(Config):
	DEBUG = True
	TESTING = True
	IP_HOST = 'localhost'
	PORT_HOST = 5000
	SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.abspath("storage.db")}'

class ConfigTesting(Config):
	DEBUG = True
	TESTING = True
	IP_HOST = 'encurtador-url-pythonic.up.railway.app' # Cloud Server
	PORT_HOST = 80
	SQLALCHEMY_DATABASE_URI = 'mysql://root:OJgMdk2lrbvpgFXde6po@containers-us-west-47.railway.app:5988/railway' # Temporary DB
	
class ConfigProduction(Config):
	DEBUG = False
	TESTING = False
	IP_HOST = 'encurtador-url-pythonic.up.railway.app' # Cloud Server
	PORT_HOST = 80
	SQLALCHEMY_DATABASE_URI = 'mysql://root:OJgMdk2lrbvpgFXde6po@containers-us-west-47.railway.app:5988/railway' # Temporary DB
	
app_config = {
		'development': ConfigDevelopment,
		'testing': ConfigTesting,
		'production': ConfigProduction	
	}

server_mode = environ['FLASK_ENV']

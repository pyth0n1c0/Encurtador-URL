from app import create_app
from config import app_config, server_mode

config = app_config[server_mode]
app = create_app(config, server_mode)

if __name__ == '__main__':
	app.run(host=config.IP_HOST, port=config.PORT_HOST, debug=config.DEBUG)

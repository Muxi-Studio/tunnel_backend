#encoding: utf-8

from config import config
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


mail = Mail()
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)



def create_app(config_name=None):
    if config_name is None:
        config_name = 'default'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        db.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


from .api_1_0 import api
app.register_blueprint(api, url_prefix='/api')




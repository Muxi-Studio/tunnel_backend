#encoding: utf-8

from config import config
from flask_mail import Mail
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()


def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = 'production'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    with app.app_context():
        db.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app(config_name = 'default')
mails = Mail(app)


from .api_1_0 import api
app.register_blueprint(api, url_prefix='/api')




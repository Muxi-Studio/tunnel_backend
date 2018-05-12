#encoding: utf-8

from . import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


from .api_1_0 import api
app.register_blueprint(api, url_prefix='/api')




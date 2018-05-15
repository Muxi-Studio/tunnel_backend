#encoding: utf-8
import os

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = os.environ.get('mysqlpassword')
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_tunnel'
DATABASETest = 'ts'



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard ot guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    MAIL_SEREVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                           DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                           DATABASE)

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                           DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                           DATABASE)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                                                                           DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                           DATABASE)

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

config={
    'developments': DevelopmentConfig,
    'testing': TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
#encoding: utf-8

from flask_script import Manager, Shell
from app import app, db
from app.models import Message

manager = Manager(app)

@manager.command
def createdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()
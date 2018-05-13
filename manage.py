#encoding: utf-8

from flask_script import Manager, Shell
from app import app, db

manager = Manager(app)

@manager.command
def createdb():
    db.create_all()


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
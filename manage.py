#encoding: utf-8

from flask_script import Manager, Shell
from app import app, db
from flask_migrate import Migrate, MigrateCommand
from app.models import Message
import os

manager = Manager(app)

'''
init 初始化一个数据库
migrage  迁移文件
update  生成新的表
'''


#使用flask_migrate必须绑定app和db
migrate = Migrate(app, db)


#把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

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
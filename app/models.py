# encoding: utf-8
from . import db


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.String(15), nullable=False)
    way = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<content %r>' % self.content

    def __repr__(self):
        return '<time %r>' % self.time

    def __repr__(self):
        return '<way %r>' % self.way

    def __repr__(self):
        return '<name %r>' % self.name

    def __repr__(self):
        return '<address %r>' % self.address
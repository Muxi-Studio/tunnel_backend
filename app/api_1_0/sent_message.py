from . import api
from flask import request, jsonify, session
from ..models import Message as ME
from flask_mail import Message, Mail
from .. import app, db
import os

app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mails = Mail(app)

def msg_dict2(to, subject, body, **kwargs):
    msg = Message(
        subject='come from ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = body
    msg.html = body
    return msg.__dict__

def send_async_email(msg_dict):
    with app.app_context():
        msg = Message()
        msg.__dict__.update(msg_dict)
        mails.send(msg)


@api.route('/sent/<int:id>/', methods=['POST'])
def sent(id):
    token1 = request.headers['token']
    token = session.get('token')
    if token == token1:
        mess = ME.query.filter_by(id=id).first()
        if mess.way == 1:
            try:
                send_async_email(msg_dict2(mess.address, mess.name, mess.content))
                mess.status = 2
                db.session.add(mess)
                db.session.commit()
                return jsonify({}), 200
            except:
                mess.status = 2
                db.session.add(mess)
                db.session.commit()
                return jsonify({}), 500
        elif mess.way == 2:
            pass
    return jsonify({}), 404
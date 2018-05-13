from . import api
from flask import request, jsonify, session
from ..models import Message as ME
from flask_mail import Message, Mail
from .. import app
import os

app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


def msg_dict2(to, subject, body, **kwargs):
    mails = Mail(app)
    msg = Message(
        subject='come from ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = body
    msg.html = body
    print body
    mails.send(msg)


@api.route('/sent/<int:id>/', methods=['POST'])
def sent(id):
    token1 = request.headers['token']
    token = session.get('token')
    if token == token1:
        mess = ME.query.filter_by(id=id).first()
        if mess.way == 1:
            try:
                msg_dict2(mess.address, mess.name, mess.content)
                return jsonify({}), 200
            except:
                return jsonify({}), 500
        elif mess.way == 2:
            pass
    return jsonify({}), 404
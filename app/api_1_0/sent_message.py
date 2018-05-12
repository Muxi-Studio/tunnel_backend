from . import api
from flask import request, jsonify, session
from ..models import Message as ME
from flask_mail import Message, Mail
from .. import app

app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = 'testforflask@126.com'
app.config['MAIL_PASSWORD'] = 't123654789'


def msg_dict2(to, subject, body, **kwargs):
    mails = Mail(app)
    msg = Message(
        subject='come from ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = body
    msg.html = body
    mails.send(msg)


@api.route('/sent/<int:id>/', methods=['POST'])
def sent(id):
    token1 = request.headers['token']
    token = session.get('token')
    if token == token1:
        mess = ME.query.filter_by(id=id).first()
        msg_dict2(mess.address, mess.name, mess.content)
        return jsonify({}), 200
    return jsonify({}), 404
# coding: utf-8
from . import api
from flask import request, jsonify, session, current_app
from ..models import Message as ME
from flask_mail import Message, Mail
from .. import app, db
import os
from config import config
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



def confirm(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if data.get('id') != 1:
        return False
    return True

# app.config['MAIL_SERVER'] = 'smtp.qq.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config.from_object(config['production'])

mails = Mail(app)

def msg_dict2(to, subject, body, **kwargs):
    msg = Message(
        subject='来自一直惦记着你的' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = body + '\n' + '华大桂声与你同行'
    msg.html = body + '\n' + '华大桂声与你同行'
    try:
        with app.open_resource("/tmp/" + str(ID) + ".jpg","rb") as fp:
            msg.attach("image.jpg", "image/jpg", fp.read())
        with app.open_resource("/tmp/" + str(ID) + ".wav","rb") as fp:
            msg.attach("voice.wav", "mp3/wav", fp.read())
    except:
        pass
    return msg.__dict__

def send_async_email(msg_dict):
    with app.app_context():
        msg = Message()
        msg.__dict__.update(msg_dict)
        mails.send(msg)


@api.route('/sent/<int:id>/', methods=['POST'])
def sent(id):
    token = request.headers['token']
    #token1 = session.get('token')
    #if token == token1:
    global ID
    ID = id
    if confirm(token):
        mess = ME.query.filter_by(id=id).first()
        if mess.way == 2:
            try:
                send_async_email(msg_dict2(mess.address, mess.name, mess.content))
                mess.status = 2
                db.session.add(mess)
                db.session.commit()
                return jsonify({}), 200
            except Exception,e:
                print(e)
                mess.status = 3
                db.session.add(mess)
                db.session.commit()
                return jsonify({}), 500
        elif mess.way == 1:
            pass
    return jsonify({}), 404

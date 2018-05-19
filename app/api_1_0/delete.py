#encoding: utf-8
from . import api
from flask import request, jsonify, session
from app import db
from ..models import Message
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



@api.route('/admin/message/<id>/', methods=['DELETE'])
def delete(id):
    token = request.headers['token']
    token1 = session.get('token')
    #if token1 == token:
    if confirm(token):
        try:
            mess = Message.query.filter_by(id=id).first()
            mess.status = 4
            db.session.add(mess)
            db.session.commit()
            return jsonify({
            }), 200
        except:
            return jsonify({
            }), 500
    else:
        return jsonify({
        }), 403


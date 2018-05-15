#encoding: utf-8
from . import api
from flask import request, jsonify, session
from app import db
from ..models import Message


@api.route('/admin/message/<id>/', methods=['DELETE'])
def delete(id):
    token = request.headers['token']
    token1 = session.get('token')
    if token1 == token:
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


# encoding: utf-8
from flask import request, jsonify, session
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import api
from config import config
import os


@api.route('/signin/', methods=['POST'])
def signin():
    username = request.values.get("username")
    password = request.values.get("password")

    s = Serializer(config["developments"].SECRET_KEY, expires_in=1800)
    token = s.dumps({'id': 1})
    session['token'] = token
    if username == os.environ.get('USERNAME') and password == os.environ.get('PASSWORD'):
        return jsonify({
            "token": token
        }), 200
    else:
        return jsonify({
        }), 401
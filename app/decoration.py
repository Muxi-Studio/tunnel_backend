#encoding: utf-8
from functools import wraps
from flask import session, jsonify


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.form['token']
        s = Serializer(config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return jsonify({'status': 'fail', 'data': {'msg': 'expired token'}})
        except BadSignature:
            return jsonify({'status': 'fail', 'data': {'msg': 'useless token'}})
        kwargs['user_id'] = data['id']
        return func(*args, **kwargs)
    return wrapper


#登录限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id') == token:
            return func(*args, **kwargs)
        else:
            return jsonify({
                "message": "fail to signin"
            }), 401
    return wrapper
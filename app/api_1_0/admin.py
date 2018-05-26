#encoding: utf-8
from . import api
from flask import request, jsonify, session, current_app
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

@api.route('/admin/pages/<int:pageNumber>/', methods=['GET'])
def pages(pageNumber):
    token = request.headers['token']
    #if session.get('token') == token:
    if 1:
        messagelist = []
        all_mess = []
        message = Message.query.all()
        message_num = len(message)
        for m in message:
            if m.status != 4:
                all_mess.append(m.id)
        all_mess.sort(reverse=True)
        try:
            mess = all_mess[(pageNumber - 1) * 15:pageNumber*15]
            test = all_mess[14]
        except:
            mess = all_mess[(pageNumber - 1) * 15:]
        for m in mess:
            mes = Message.query.filter_by(id=m).first()
            id = mes.id
            content = mes.content
            name = mes.name
            time = mes.time
            address = mes.address
            status = mes.status
            messagelist.append({"id": id,
                            "sent_content": content,
                            "sent_name": name,
                            "sent_time": time,
                            "sent_address": address,
                            "sent_status": status,
                            "message_num": message_num})
        return jsonify({
            "messagelist": messagelist
        }), 200
    else:
        return jsonify({
        }), 403




@api.route('/admin/pages/<int:pageNumber>/time/<string:time>/', methods=['GET'])
def time_page(pageNumber, time):
    token = request.headers['token']
    #if session.get('token') == token:
    if confirm(token):
        messagelist = []
        all_mess = []
        message = Message.query.all()
        message_num = len(message)
        for m in message:
            if m.time == time and m.status != 4:
                all_mess.append(m.id)
        all_mess.sort(reverse=True)
        try:
            mess = all_mess[(pageNumber - 1) * 15:pageNumber*15]
            test = all_mess[14]
        except:
            mess = all_mess[(pageNumber - 1) * 15:]
        for m in mess:
            mes = Message.query.filter_by(id=m).first()
            id = mes.id
            content = mes.content
            name = mes.name
            time = mes.time
            address = mes.address
            status = mes.status
            messagelist.append({"id": id,
                                "sent_content": content,
                                "sent_name": name,
                                "sent_time": time,
                                "sent_address": address,
                                "sent_status": status,
                                "message_num": message_num})
        return jsonify({
            "messagelist": messagelist
        }), 200
    else:
        return jsonify({
        }), 403


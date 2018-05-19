# encoding:utf-8
import base64
import unittest
from flask import current_app, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from app.models import Message
from app import create_app
import json
import os

db = SQLAlchemy()

token = str(0)
id = int(0)
pageNumber = int(0)
time = str(0)


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

        from app.api_1_0 import api
        self.app.register_blueprint(api, url_prefix='/api')

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)

    # ----------API FILE NAME:api_1_0/signin.py-------------------

    # Test signin
    def test_a_signin(self):
        response = self.client.post(
            url_for('api.signin', _external=True),
            data=json.dumps({
                "username": "TStunnel",
                "password": "Ilovemuxi"
            }),
            content_type='application/json')
        s = json.loads(response.data)['token']
        global token
        token = s
        self.assertTrue(response.status_code == 200)

    # ----------API FILE NAME:api_1_0/delete.py-------------------

    # Test delete
    def test_c_delete(self):
        response = self.client.delete(
            url_for('api.delete', id=1, _external=True),
            headers={
                "token": token,
            },
            content_type='application/json')
        self.assertTrue(response.status_code == 200)

    # ----------API FILE NAME:api_1_0/User.py-------------------

    # Test message
    def test_a_message(self):
        response = self.client.post(
            url_for('api.message', _external=True),
            data=json.dumps({
                "sent_content": "this is content of the eamil",
                "sent_name": "darren",
                "sent_time": "sent_time1",
                "sent_address": "17362990052@163.com"
            }),
            content_type='application/json')
        self.assertTrue(response.status_code == 200)

    # ----------API FILE NAME:api_1_0/__init__.py-------------------

    # ----------API FILE NAME:api_1_0/admin.py-------------------

    # Test pages
    def test_c_pages(self):
        response = self.client.get(
            url_for('api.pages', pageNumber=1, _external=True),
            headers={
                "token": token,
            },
            content_type='application/json')
        self.assertTrue(response.status_code == 200)

    # Test time_page
    def test_c_time_page(self):
        response = self.client.get(
            url_for('api.time_page', pageNumber=1, time='sent_time1', _external=True),
            headers={
                "token": token,
            },
            content_type='application/json')
        self.assertTrue(response.status_code == 200)

    # ----------API FILE NAME:api_1_0/sent_message.py-------------------

    # Test sent
    def test_c_sent(self):
        response = self.client.post(
            url_for('api.sent', id=1, _external=True),
            headers={
                "token": token,
            },
            content_type='application/json')
        self.assertTrue(response.status_code == 200)

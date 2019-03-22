from flask import request
from . import auth
from ..model import UserInfo
from ..router import Response_headers
from .. import db

import json
import random
import string


@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userinfo = json.loads(request.get_data().decode("utf-8"))
        phone = userinfo['phone']
        password = userinfo['password']

        user = UserInfo.query.filter_by(phone=phone).first()
        if user and user.password == password:
            resp = Response_headers(200, {'status': 1})
            resp.set_cookie('userid', str(user.id))
            resp.set_cookie('username', str(user.name))
        else:
            resp = Response_headers(200, {'status': 0})
        return resp
    else:
        resp = Response_headers(405, {})
        return resp


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        userinfo = json.loads(request.get_data().decode("utf-8"))
        phone = userinfo['phone']
        password = userinfo['password']

        user = UserInfo.query.filter_by(phone=phone).first()
        # 用户名存在
        if user:
            resp = Response_headers(202, {'status': 0, 'message': '账号已存在'})
            return resp
        else:
            try:
                name = ''.join(random.sample(
                    string.ascii_letters + string.digits, 8))
                user = UserInfo(
                    phone=str(phone),
                    password=str(password),
                    name=name,
                    credit=0,
                    rest=0,
                    income=0
                )
                db.session.add(user)
                db.session.commit()
                resp = Response_headers(
                    201, {'status': 1, 'message': '账号创建成功'})
                return resp
            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '请检查参数类型'})
                return resp

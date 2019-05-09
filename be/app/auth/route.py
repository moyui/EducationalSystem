from flask import request
from . import auth
from ..model import UserInfo
from ..router import Response_headers
from ..decorator import is_login
from .. import db
from decimal import *

import json
import random
import string


@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userinfo = json.loads(request.get_data().decode("utf-8"))
        mail = userinfo['mail']
        password = userinfo['password']

        user = UserInfo.query.filter_by(mail=mail).first()
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
        mail = userinfo['mail']
        password = userinfo['password']
        name = userinfo['userName'] or ''.join(random.sample(
            string.ascii_letters + string.digits, 8))

        user = UserInfo.query.filter_by(mail=mail).first()
        # 用户名存在
        if user:
            resp = Response_headers(202, {'status': 0, 'message': '账号已存在'})
            return resp
        else:
            try:
                user = UserInfo(
                    mail=str(mail),
                    password=str(password),
                    name=str(name),
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


@auth.route('/userinfo', methods=['GET'])
@is_login
def userinfo(userid):
    if request.method == 'GET':
        if userid is not None:
            try:
                userinfo = UserInfo.query.filter_by(
                    id=int(userid)).first()
                return Response_headers(200,
                                        {'status': 1,
                                         'data':
                                         {'id': userinfo.id,
                                          'mail': userinfo.mail,
                                          'name': userinfo.name,
                                          'credit': userinfo.credit,
                                          'rest':  "%.2f" % userinfo.rest,
                                          'income': "%.2f" % userinfo.income
                                          }
                                         })
            except Exception as e:
                print(e)
                return Response_headers(500, {'status': 0, 'message': '用户名无效或服务器暂时不可用'})
        else:
            return Response_headers(401, {'status': 2, 'message': '您尚未登录，请您先登录'})
    else:
        return Response_headers(405, {'status': 0})

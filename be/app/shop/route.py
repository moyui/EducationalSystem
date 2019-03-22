from flask import request
from . import shop
from ..router import Response_headers
from ..decorator import is_login
from ..model import UserOrder, UserInfo, UserDeposit, CourseInfo
from .. import db
from money import Money

import json
import time


@shop.route('/shop/order', methods=['POST'])
@is_login
def order(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                courseinfo = json.loads(request.get_data().decode("utf-8"))
                courseid = int(courseinfo['id'])

                order = UserOrder.query.filter_by(
                    userid=int(userid), courseid=courseid).first()

                # 说明已经有订单了
                if order is not None:
                    resp = Response_headers(202, {'status': 1})
                    return resp
                else:
                    orderinfo = UserOrder(
                        userid=int(userid),
                        courseid=courseid,
                        createdate=str(time.time()),
                        finishdate='',
                        statusid=1
                    )
                    db.session.add(orderinfo)
                    db.session.commit()
                    resp = Response_headers(201, {'status': 1})
                    return resp

            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '服务器错误，请稍后再试'})
                return resp
        else:
            resp = Response_headers(
                401, {'status': 2, 'message': '您尚未登录，请您先登录'})
            return resp
    else:
        resp = Response_headers(405, {})
        return resp


@shop.route('/shop/purchase', methods=['POST'])
@is_login
def purchase(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                courseinfo = json.loads(request.get_data().decode("utf-8"))
                courseid = int(courseinfo['id'])
                payway = int(courseinfo['payway'])

                order = UserOrder.query.filter_by(
                    userid=int(userid), courseid=courseid).first()

                # 已有订单记录并且等待支付转入正常流程
                if order is not None and order.statusid == 1:
                    # 如果是从余额扣款
                    if payway == 1:
                        userinfo = UserInfo.query.filter_by(
                            id=int(userid)).first()
                        course = CourseInfo.query.filter_by(
                            id=courseid).first()

                        # 金额大于
                        if userinfo.rest >= course.price:
                            userinfo.rest = (Money(
                                str(userinfo.rest), 'RMB') - Money(str(course.price), 'RMB')).amount
                            # 修改id
                            order.statusid = int(2)
                            db.session.commit()
                            deposit = UserDeposit(
                                userid=int(userid),
                                amount=Money(str(course.price), 'RMB'),
                                createdate=str(time.time()),
                                fromid=payway
                            )
                            db.session.add(deposit)
                            db.session.commit()

                            resp = Response_headers(
                                201, {'status': 1, 'message': '扣款成功'})
                            return resp
                        else:
                            resp = Response_headers(
                                403, {'status': 3, 'message': '余额不足，请直接扣款'}
                            )
                            return resp
                    # 如果是直接扣款
                    elif payway == 2:
                        course = CourseInfo.query.filter_by(
                            id=courseid).first()
                        order.statusid = int(2)
                        deposit = UserDeposit(
                            userid=int(userid),
                            amount=Money(str(course.price), 'RMB').amount,
                            createdate=str(time.time()),
                            fromid=payway
                        )
                        db.session.add(deposit)
                        db.session.commit()

                        resp = Response_headers(
                            201, {'status': 1, 'message': '支付成功'})
                        return resp
                    else:
                        resp = Response_headers(
                            403, {'status': 0, 'message': '扣款方式错误'})
                        return resp

                else:
                    resp = Response_headers(
                        403, {'status': 0, 'message': '订单不存在或者已经支付'})
                    return resp

            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '服务器错误，请稍后再试'})
                return resp
        else:
            resp = Response_headers(
                401, {'status': 2, 'message': '您尚未登录，请想先登录'})
            return resp
    else:
        resp = Response_headers(405, {})
        return resp

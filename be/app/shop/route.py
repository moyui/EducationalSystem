from flask import request
from . import shop
from ..router import Response_headers
from ..decorator import is_login
from ..model import UserOrder, UserInfo, UserDeposit, CourseInfo, PayWay, UserDeposit, RestInfo, OrderStatus, UserDistribution,  UserDistributionDetail, VideoInfo, UserProgress, UserWithDrawMoney
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
                    userid=int(userid), courseid=courseid, statusid=1).first()

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
                link = str(courseinfo['link'])

                order = UserOrder.query.filter_by(
                    userid=int(userid), courseid=courseid, statusid=1).first()

                # 已有订单记录并且等待支付转入正常流程
                if order is not None:
                    # 这里判断用户的余额是否大于扣款金额
                    userinfo = UserInfo.query.filter_by(id=int(userid)).first()
                    course = CourseInfo.query.filter_by(id=courseid).first()
                    if payway == 1:
                        # 如果可以从余额扣款
                        if userinfo.rest > course.price:
                            userinfo.rest = (Money(
                                str(userinfo.rest), 'RMB') - Money(str(course.price), 'RMB')).amount
                            # 修改id
                            order.statusid = int(2)
                            db.session.commit()
                            # 加入付款单
                            deposit = UserDeposit(
                                userid=int(userid),
                                amount=Money(str(course.price), 'RMB').amount,
                                createdate=str(time.time()),
                                fromid=payway
                            )
                            # 加入余额单
                            rest = RestInfo(
                                userid=int(userid),
                                amount=course.price,
                                createdate=str(time.time()),
                                payway=4,
                                distribute=-1
                            )

                            # 课程购买人数+1
                            course.buynum = course.buynum + 1

                            db.session.add(deposit)
                            db.session.add(rest)
                            db.session.commit()

                            # 计算课程分销
                            if link != '':
                                price = (Money(
                                    str(course.price), 'RMB') * 5 / 100)

                                distributeQ = UserDistribution.query.filter_by(
                                    link=str(link)).first()

                                otherinfo = UserInfo.query.filter_by(
                                    id=int(distributeQ.userid)).first()
                                otherinfo.rest = (Money(
                                    str(userinfo.rest), 'RMB') + price).amount

                                rest = RestInfo(
                                    userid=int(distributeQ.userid),
                                    amount=price.amount,
                                    createdate=str(time.time()),
                                    payway=3,
                                    distribute=-1
                                )
                                udetail = UserDistributionDetail(
                                    distributioniod=distributeQ.id,
                                    orderid=int(order.id),
                                    income=price.amount,
                                    userid=int(userid)
                                )
                                db.session.add(rest)
                                db.session.add(udetail)
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
                        order.statusid = int(2)
                        deposit = UserDeposit(
                            userid=int(userid),
                            amount=Money(str(course.price), 'RMB').amount,
                            createdate=str(time.time()),
                            fromid=payway
                        )

                        # 课程购买人数+1
                        course.buynum = course.buynum + 1

                        db.session.add(deposit)
                        db.session.commit()

                        # 计算课程分销
                        if link != '':
                            price = (Money(
                                str(course.price), 'RMB') * 5 / 100)

                            distributeQ = UserDistribution.query.filter_by(
                                link=str(link)).first()

                            otherinfo = UserInfo.query.filter_by(
                                id=int(distributeQ.userid)).first()
                            otherinfo.rest = (Money(
                                str(userinfo.rest), 'RMB') + price).amount

                            rest = RestInfo(
                                userid=int(distributeQ.userid),
                                amount=price.amount,
                                createdate=str(time.time()),
                                payway=3,
                                distribute=-1
                            )
                            udetail = UserDistributionDetail(
                                distributioniod=distributeQ.id,
                                orderid=int(order.id),
                                income=price.amount,
                                userid=int(userid)
                            )
                            db.session.add(rest)
                            db.session.add(udetail)
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


@shop.route('/shop/payway', methods=['GET'])
def payway():
    if request.method == 'GET':
        payArr = []
        try:
            payway = PayWay.query.all()

            for item in payway:
                payArr.append({
                    'id': item.id,
                    'name': item.name
                })
            return Response_headers(200, {'status': 1, 'payway': payArr})
        except Exception as e:
            print(e)
            return Response_headers(500, {})
    else:
        return Response_headers(405, {})


@shop.route('/shop/recharge', methods=['POST'])
@is_login
def recharge(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                rechargeInfo = json.loads(request.get_data().decode("utf-8"))
                payway = int(rechargeInfo['payway'])
                amount = Money(str(rechargeInfo['amount']), "RMB")

                rest = RestInfo(
                    userid=int(userid),
                    amount=amount.amount,
                    createdate=str(time.time()),
                    payway=payway,
                    distribute=-1
                )

                userinfo = UserInfo.query.filter_by(
                    id=int(userid)).first()
                userinfo.rest = (Money(
                    str(userinfo.rest), 'RMB') + amount).amount

                db.session.add(rest)
                db.session.commit()
                resp = Response_headers(
                    201, {'status': 1, 'message': '支付成功'})
                return resp
            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '服务器错误，请稍后再试'})
                return resp
    else:
        return Response_headers(405, {})


@shop.route('/shop/restList', methods=['GET'])
@is_login
def restList(userid):
    if request.method == 'GET':
        restArr = []
        if userid is not None:
            try:
                restinfo = RestInfo.query.filter_by(userid=userid).all()
                for item in restinfo:
                    restArr.append({
                        'id': item.id,
                        'amount': "%.2f" % item.amount,
                        'createdate': item.createdate,
                        'payway': item.payway,
                        'distribute': item.distribute
                    })
                resp = Response_headers(
                    200, {'status': 1, 'restlist': restArr})
                return resp
            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '服务器错误，请稍后再试'})
                return resp
    else:
        return Response_headers(405, {})


@shop.route('/orderList', methods=['GET'])
@is_login
def orderlist(userid):
    if request.method == 'GET':
        orderArr = []
        if userid is not None:
            try:
                courseinfo = CourseInfo.query.all()
                coursedict = {}
                for item in courseinfo:
                    coursedict[item.id] = {
                        'name': item.name,
                        'price': item.price
                    }

                statusinfo = OrderStatus.query.all()
                statusdict = {}
                for item in statusinfo:
                    statusdict[item.id] = item.name

                orderinfo = UserOrder.query.filter_by(userid=userid).all()
                for item in orderinfo:
                    orderArr.append({
                        'id': item.id,
                        'courseid': item.courseid,
                        'coursename': coursedict[item.courseid]['name'],
                        'statusid': item.statusid,
                        'statusname': statusdict[item.statusid],
                        'createdate': item.createdate,
                        'finishdate': item.finishdate,
                        'price': "%.2f" % coursedict[item.courseid]['price']
                    })

                resp = Response_headers(
                    200, {'status': 1, 'orderlist': orderArr})
                return resp
            except Exception as e:
                print(e)
                resp = Response_headers(
                    500, {'status': 0, 'message': '服务器错误，请稍后再试'})
                return resp
    else:
        return Response_headers(405, {})


@shop.route('/distribution', methods=['POST'])
@is_login
def distribution(userid):
    if request.method == 'POST':
        distribution = json.loads(request.get_data().decode("utf-8"))
        courseid = int(distribution['id'])

        distributionA = UserDistribution(
            userid=int(userid),
            courseid=int(courseid),
            radio=Money('0.05', 'RMB').amount,
            link=str(int(time.time()*1000000)),
            isopen=True
        )
        db.session.add(distributionA)
        db.session.commit()
        resp = Response_headers(200, {'status': 1})
        return resp
    else:
        return Response_headers(405, {})


@shop.route('/getdistribution', methods=['GET'])
@is_login
def getdistribution(userid):
    if request.method == 'GET':
        back = []
        distributionQ = UserDistribution.query.filter_by(
            isopen=True, userid=int(userid)).all()
        for item in distributionQ:

            courseinfoQ = CourseInfo.query.filter_by(id=item.courseid).first()

            backA = {}
            backA['id'] = item.id
            backA['link'] = item.link
            backA['coursename'] = courseinfoQ.name
            backA['courseid'] = courseinfoQ.id
            backA['detail'] = []

            distributionDetailQ = UserDistributionDetail.query.filter_by(
                distributioniod=item.id
            ).all()

            for itemA in distributionDetailQ:
                user = UserInfo.query.filter_by(id=itemA.userid).first()
                order = UserOrder.query.filter_by(id=itemA.orderid).first()

                backA['detail'].append({
                    'id': itemA.id,
                    'orderid': itemA.orderid,
                    'income': "%.2f" % itemA.income,
                    'username': user.name,
                    'radio': '5%',
                    'createdate': order.createdate
                })

            back.append(backA)
        resp = Response_headers(200, {'status': 1, 'back': back})
        return resp
    else:
        return Response_headers(405, {})


@shop.route('/closedistribution', methods=['POST'])
def closedistribution():
    distribution = json.loads(request.get_data().decode("utf-8"))
    id = int(distribution['id'])
    distributionQ = UserDistribution.query.filter_by(
        isopen=True, id=int(id)).order_by(UserDistribution.id.desc()).first()
    distributionQ.isopen = False
    db.session.commit()
    resp = Response_headers(201, {'status': 1})
    return resp


@shop.route('/withdraw', methods=['POST'])
@is_login
def withdraw(userid):
    if request.method == 'POST':
        withdraw = json.loads(request.get_data().decode("utf-8"))
        orderid = int(withdraw['id'])

        # 首先判断能否退课，即用户已经学完了所有视频
        userorder = UserOrder.query.filter_by(id=int(orderid)).first()

        videoQ = VideoInfo.query.filter_by(courseid=userorder.courseid).all()

        total = 0
        have = 0

        for itemV in videoQ:
            total = total + 1

            progQ = UserProgress.query.filter_by(
                userid=userid, videoid=itemV.id, courseid=userorder.courseid).order_by(UserProgress.id.desc()).first()

            if progQ is not None:
                have = have + 1
        
        courseinfo = CourseInfo.query.filter_by(
                id=userorder.courseid).first()
        price = (Money(str(courseinfo.price), 'RMB'))

        if have == total:
            resp = Response_headers(
                404, {'status': 0, 'message': '您已看过所有视频，无法退课'})
            return resp
        elif total > 0 and have == 0:

            withdrawA = UserWithDrawMoney(
                userid=int(userid),
                orderid=userorder.id,
                money=price.amount
            )
            userinfo = UserInfo.query.filter_by(id=int(userid)).first()
            userorder.statusid = 4
            userinfo.rest = (Money(str(userinfo.rest), 'RMB') + price).amount
            rest = RestInfo(
                userid=int(userid),
                amount=price.amount,
                createdate=str(time.time()),
                payway=5,
                distribute=-1
            )

            db.session.add(withdrawA)
            db.session.add(rest)
            db.session.commit()

            resp = Response_headers(200, {'status': 1})
            return resp
        else:
            pricerest = price / total * (total - have)
            withdrawA = UserWithDrawMoney(
                userid=int(userid),
                orderid=userorder.id,
                money=pricerest.amount
            )
            userinfo = UserInfo.query.filter_by(id=int(userid)).first()
            userorder.statusid = 4
            userinfo.rest = (Money(str(userinfo.rest), 'RMB') + pricerest).amount
            rest = RestInfo(
                userid=int(userid),
                amount=pricerest.amount,
                createdate=str(time.time()),
                payway=5,
                distribute=-1
            )
            db.session.add(withdrawA)
            db.session.add(rest)
            db.session.commit()
            
            resp = Response_headers(200, {'status': 1})
            return resp
    else:
        return Response_headers(405, {})

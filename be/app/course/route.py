from flask import request
from . import course
from ..model import CourseGroup, CourseVariety, CourseClassify, CourseInfo, TeacherInfo, TeacherConnect, ConnectType, CourseTag, TagVariety, CourseTime, CourseMenu, UserOrder, VideoInfo, UserInfo, UserProgress, CourseTest, UserAnswer, UserQualify, UserHoner, HonerType
from ..router import Response_headers
from ..decorator import is_login
from .. import db

import json
import time


@course.route('/course/classify', methods=['GET'])
def classify():
    if request.method == 'GET':
        groupArr = []
        varietyArr = []
        try:
            group = CourseGroup.query.all()
            variety = CourseVariety.query.all()

            for item in group:
                groupArr.append({
                    'id': item.id,
                    'name': item.name
                })

            for item in variety:
                varietyArr.append({
                    'id': item.id,
                    'name': item.name,
                    'group_id': item.groupid
                })

            return Response_headers(200, {'status': 1, 'data': {'group': groupArr, 'variety': varietyArr}})
        except Exception as e:
            print(e)
            return Response_headers(500, {})
    else:
        return Response_headers(405, {})


@course.route('/course/list', methods=['GET'])
def courseList():
    if request.method == 'GET':
        varietyid = request.args.get('varietyid')
        courseArr = []
        try:
            courseMid = CourseClassify.query.filter_by(
                variety=int(varietyid)).all()
            for item in courseMid:
                course = CourseInfo.query.filter_by(
                    id=item.courseid).first()
                teacher = TeacherInfo.query.filter_by(
                    id=course.teacherid).first()
                courseArr.append({
                    'id': course.id,
                    'name': course.name,
                    'teacher': teacher.name,
                    'logo': course.mainimg,
                    'price': str(course.price)
                })
            return Response_headers(200, {'status': 1, 'list': courseArr})
        except Exception as e:
            print(e)
            return Response_headers(500, {})
    else:
        return Response_headers(405, {})


@course.route('/course/view', methods=['GET'])
@is_login
def courseView(userid):
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            course = CourseInfo.query.filter_by(id=int(id)).first()
            teacher = TeacherInfo.query.filter_by(
                id=course.teacherid).first()

            connect = []

            tags = []

            time = []

            menu = []

            hasTotal = 0

            learningTotal = 0

            isBought = False

            connectQ = TeacherConnect.query.filter_by(
                teacherid=int(teacher.id)).all()

            tagsQ = CourseTag.query.filter_by(courseid=int(course.id)).all()

            timeQ = CourseTime.query.filter_by(courseid=int(course.id)).all()

            menuQ = CourseMenu.query.filter_by(courseid=int(course.id)).all()

            orderQ = UserOrder.query.filter_by(userid=int(userid or -1), courseid=int(
                course.id)).order_by(UserOrder.id.desc()).first()

            courseTotalQ = CourseInfo.query.filter_by(
                teacherid=int(teacher.id)).all()

            for item in connectQ:
                connectType = ConnectType.query.filter_by(
                    id=int(item.typeid)
                ).first()

                connect.append({
                    'type': connectType.name,
                    'value': item.value
                })

            for item in tagsQ:
                tagType = TagVariety.query.filter_by(
                    id=int(item.tagid)
                ).first()
                tags.append(tagType.name)

            for item in timeQ:
                time.append(item.time)

            for item in menuQ:
                menu.append({
                    'id': item.id,
                    'title': item.title,
                    'video': []
                })

            for item in courseTotalQ:
                hasTotal = hasTotal + 1
                learningTotal = learningTotal + int(item.buynum)

            for item in menu:
                videoQ = VideoInfo.query.filter_by(
                    menuid=int(item['id'])).all()

                for videoItem in videoQ:
                    item['video'].append({
                        'id': videoItem.id,
                        'totaltime': videoItem.totaltime,
                        'title': videoItem.title,
                        'url': videoItem.url,
                        'picurl': videoItem.picurl
                    })

            if orderQ is not None and orderQ.statusid == 2:
                isBought = True

            basic = {
                'id': course.id,
                'name': course.name,
                'price': str(course.price),
                'info': course.info,
                'extra_info': course.extrainfo,
                'total': course.buynum,
                'favour': course.favour,
                'last': course.courselast,
                'logo': course.mainimg
            }
            teacher = {
                'name': teacher.name,
                'id': teacher.id,
                'info': teacher.info,
                'connect': connect,
                'has_total': hasTotal,
                'learning_total': learningTotal
            }

            detail = {
                'tags': tags,
                'time': time,
                'menu': menu,
                'isbought': isBought
            }
            return Response_headers(200, {'status': 1, 'data': {'basic': basic, 'teacher': teacher, 'detail': detail}})
        except Exception as e:
            print(e)
            return Response_headers(500, {})
    else:
        return Response_headers(405, {})


@course.route('/course/cantest', methods=['GET'])
@is_login
def cantest(userid):
    if request.method == 'GET' and userid is not None:
        id = request.args.get('id')
        total = 0

        MenuInfo = CourseMenu.query.filter_by(courseid=int(id)).all()
        for item in MenuInfo:
            temp = VideoInfo.query.filter_by(menuid=int(item.id)).count()
            total = total + temp

        Progress = UserProgress.query.filter_by(
            courseid=int(id), userid=int(userid)).count()

        cantest = False
        if Progress >= total:
            cantest = True

        return Response_headers(200, {'status': 1, 'data': {'total': total, 'cantest': cantest}})

    else:
        return Response_headers(405, {})


@course.route('/course/table', methods=['GET'])
@is_login
def table(userid):
    if request.method == 'GET':
        back = []
        # 用户可用的订单
        userorder = UserOrder.query.filter_by(userid=userid, statusid=2).all()

        # 订单对应的视频
        for itemU in userorder:

            courseQ = CourseInfo.query.filter_by(id=itemU.courseid).first()

            video = []
            videoQ = VideoInfo.query.filter_by(courseid=itemU.courseid).all()

            for itemV in videoQ:
                videoItem = {}
                videoItem['id'] = itemV.id
                videoItem['totaltime'] = itemV.totaltime
                videoItem['title'] = itemV.title

                # 判断有没有学习过
                progQ = UserProgress.query.filter_by(
                    userid=userid, videoid=itemV.id, courseid=itemU.courseid).order_by(UserProgress.id.desc()).first()
                if progQ is None:
                    videoItem['isWatch'] = '否'
                else:
                    videoItem['isWatch'] = '是'

                video.append(videoItem)

            back.append({
                'courseid': courseQ.id or '无课程',
                'coursename': courseQ.name,
                'video': video
            })

        return Response_headers(200, {'status': 1, 'data': back})

    else:
        return Response_headers(405, {})


@course.route('/question', methods=['GET'])
@is_login
def question(userid):
    if request.method == 'GET':
        courseid = int(request.args.get('courseid'))
        videoid = int(request.args.get('videoid'))
        typeid = int(request.args.get('type'))

        back = {}

        coursetestQ = CourseTest.query.filter_by(
            courseid=courseid, typeid=typeid, videoid=videoid).order_by(CourseTest.id.desc()).first()

        back['id'] = coursetestQ.id
        back['question'] = coursetestQ.question
        back['choice'] = coursetestQ.choice

        return Response_headers(200, {'status': 1, 'data': back})

    else:
        return Response_headers(405, {})


@course.route('/answer', methods=['POST'])
@is_login
def answer(userid):
    if request.method == 'POST':
        answer = json.loads(request.get_data().decode("utf-8"))
        answerG = answer['answer']
        courseid = int(answer['courseid'])
        id = int(answer['testid'])

        try:

            coursetestQ = CourseTest.query.filter_by(id=id).first()

            answerQ = coursetestQ.answer

            answerDict = str(answerQ).split('&')

            score = 0

            start = 0

            for item in answerDict:

                itemS = str(item).split(';')

                if str(itemS[0]) == str(answerG[start]):
                    score = score + int(itemS[1])

                start = start + 1

            back = {
                'score': score
            }

            answerA = UserAnswer(
                userid=int(userid),
                coursetestid=int(id),
                courseid=int(courseid),
                answer='&'.join(answerG),
                score=str(score)
            )
            db.session.add(answerA)
            db.session.commit()

            if int(score) >= 60:
                qualifyA = UserQualify(
                    createdate=str(time.time()),
                    userid=int(userid),
                    answerid=(answerA.id)
                )
                db.session.add(qualifyA)
                db.session.commit()

                addhoner('-1', courseid, -1, userid)

            return Response_headers(200, {'status': 1, 'data': back})
        except Exception as e:
            print(e)
            return Response_headers(500, {})

    else:
        return Response_headers(405, {})


def addhoner(typeid, courseid, videoid, userid):
    if str(typeid) == '-1':
        # 期末成就
        userhoner = UserHoner(
            userid=int(userid),
            courseid=int(courseid),
            typeid=1,
            videoid=-1,
            createdate=str(time.time())
        )
        db.session.add(userhoner)
        db.session.commit()


@course.route('/honer', methods=['GET'])
@is_login
def honer(userid):
    if request.method == 'GET':
        honertypeQ = HonerType.query.all()
        courseInfoQ = CourseInfo.query.all()

        honertypeDict = {}
        courseInfoDict = {}

        honerDict = []

        for item in honertypeQ:
            honertypeDict[item.id] = item.name

        for item in courseInfoQ:
            courseInfoDict[item.id] = item.name

        honerQ = UserHoner.query.filter_by(userid=int(userid)).all()

        for item in honerQ:
            honerDict.append({
                'honerid': item.id,
                'courseid': item.courseid,
                'coursename': courseInfoDict[item.courseid],
                'typeid': item.typeid,
                'typename': honertypeDict[item.typeid],
                'videoid': item.videoid,
                'createdate': item.createdate
            })

        return Response_headers(200, {'status': 1, 'data': honerDict})

    else:
        return Response_headers(405, {})

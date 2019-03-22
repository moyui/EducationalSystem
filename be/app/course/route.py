from flask import request
from . import course
from ..model import CourseGroup, CourseVariety, CourseClassify, CourseInfo, TeacherInfo, TeacherConnect, ConnectType, CourseTag, TagVariety, CourseTime, CourseMenu, UserOrder, VideoInfo
from ..router import Response_headers
from ..model import UserInfo
from ..decorator import is_login

import json


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
                videoQ = VideoInfo.query.filter_by(menuid=int(item['id'])).all()

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

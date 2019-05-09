from flask import request
from . import comment
from ..router import Response_headers
from ..decorator import is_login
from ..model import UserInfo, CourseComment
from .. import db

import json
import time


@comment.route('/comment/course/send', methods=['POST'])
@is_login
def commentCourseSend(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                commentInfo = json.loads(request.get_data().decode("utf-8"))
                courseid = commentInfo['courseid']
                comment = commentInfo['comment']

                commentA = CourseComment(
                    courseid=int(courseid),
                    userid=int(userid),
                    createdate=str(time.time()),
                    modifydate='',
                    content=comment,
                    coursetime='0',
                    addcontent='',
                    status=int(1)
                )

                db.session.add(commentA)
                db.session.commit()
                return Response_headers(201, {'status': 1})
            except Exception as e:
                print(e)
                return Response_headers(500, {'status': 0, 'message': '用户名无效或服务器暂时不可用'})
        else:
            return Response_headers(401, {'status': 2, 'message': '您尚未登录，请您先登录'})
    else:
        return Response_headers(405, {'status': 0})


@comment.route('/comment/course/sendadd', methods=['POST'])
@is_login
def commentCourseAddSend(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                commentInfo = json.loads(request.get_data().decode("utf-8"))
                courseid = commentInfo['courseid']
                addcomment = commentInfo['comment']
                isadd = commentInfo['isadd'] or False
                addbelongid = commentInfo['addbelongid'] or -1

                if isadd == False or addbelongid == -1:
                    return Response_headers(400, {'status': 0, 'message': '发送的不是追评'})

                comment = CourseComment.query.filter_by(
                    userid=int(userid),
                    courseid=int(courseid),
                    id=int(addbelongid)
                ).first()
                if comment is not None:
                    comment.addcontent = str(addcomment)
                    comment.modifydate = str(time.time())
                    db.session.commit()
                    return Response_headers(201, {'status': 1})
                else:
                    return Response_headers(404, {'status': 0, 'message': '找不到主体评论'})
            except Exception as e:
                print(e)
                return Response_headers(500, {'status': 0, 'message': '用户名无效或服务器暂时不可用'})
        else:
            return Response_headers(401, {'status': 2, 'message': '您尚未登录，请您先登录'})
    else:
        return Response_headers(405, {'status': 0})


@comment.route('/comment/course/get', methods=['GET'])
def commentCourseGet():
    if request.method == 'GET':
        try:
            id = request.args.get('id')
            commentQ = CourseComment.query.filter_by(
                courseid=int(id)).all()

            comment = []
            for item in commentQ:
                userQ = UserInfo.query.filter_by(id=int(item.userid)).first()

                comment.append({
                    'id': item.id,
                    'userid': item.userid,
                    'createdate': item.createdate,
                    'content': item.content,
                    'username': userQ.name,
                    'modifydate': item.modifydate,
                    'addcontent': item.addcontent
                })
            return Response_headers(200, {'status': 1, 'comment': comment})
        except Exception as e:
            return Response_headers(500, {'status': 0, 'message': '服务器错误'})
    else:
        return Response_headers(405, {'status': 0})

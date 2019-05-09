from flask import request
from . import video
from ..router import Response_headers
from ..decorator import is_login
from ..model import UserOrder, VideoInfo, CourseInfo, UserProgress
from .. import db

import json

@video.route('/video', methods=['GET'])
@is_login
def watch(userid):
    if request.method == 'GET':
        videoid = request.args.get('videoid')
        courseid = request.args.get('courseid')

        # 检查是不是免费课程
        courseQ = CourseInfo.query.filter_by(id=int(courseid)).first()
        videoQ = VideoInfo.query.filter_by(id=int(videoid)).first()

        # 免费课程无所谓
        if courseQ.price == -1:
            if videoQ is not None:
                video = {
                    'url': videoQ.url,
                    'picurl': videoQ.picurl,
                    'title': videoQ.title,
                    'totaltime': videoQ.totaltime
                }
                resp = Response_headers(200, {'status': 1, 'data': video})
                return resp
            else:
                resp = Response_headers(404, {'status': 0, 'meaasge': '找不到该视频'})
                return resp
        else:
            # 查找用户是否有该订单的课程
            orderQ = UserOrder.query.filter_by(userid=int(userid), courseid=int(
                courseid)).order_by(UserOrder.id.desc()).first()

            # 有订单并且付过款了
            if orderQ is not None and orderQ.statusid == 2:
                videoQ = VideoInfo.query.filter_by(id=int(videoid)).first()
                if videoQ is not None:
                    video = {
                        'url': videoQ.url,
                        'picurl': videoQ.picurl,
                        'title': videoQ.title,
                        'totaltime': videoQ.totaltime
                    }
                    resp = Response_headers(200, {'status': 1, 'data': video})
                    return resp
                else:
                    resp = Response_headers(404, {'status': 0, 'meaasge': '找不到该视频'})
                    return resp
            else:
                resp = Response_headers(
                    401, {'status': 0, 'message': '请先登录或购买后查看'})
                return resp
    else:
        return Response_headers(405, {})


@video.route('/progress', methods=['POST'])
@is_login
def progress(userid):
    if request.method == 'POST':
        if userid is not None:
            try:
                progressinfo = json.loads(request.get_data().decode("utf-8"))
                videoid = progressinfo['videoid']
                courseid = progressinfo['courseid']

                progressQ = UserProgress.query.filter_by(
                    userid=int(userid), videoid=int(videoid), courseid=int(courseid)).first()
                if progressQ is not None:
                    return Response_headers(200, {'status': 0})
                else:
                    progressA = UserProgress(
                        videoid=int(videoid),
                        userid=int(userid),
                        courseid=int(courseid)
                    )
                    db.session.add(progressA)
                    db.session.commit()
                    return Response_headers(201, {'status': 1})
            except Exception as e:
                print(e)
                return Response_headers(500, {})

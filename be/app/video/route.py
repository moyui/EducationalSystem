from flask import request
from . import video
from ..router import Response_headers
from ..decorator import is_login
from ..model import UserOrder, VideoInfo, CourseInfo
from .. import db

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
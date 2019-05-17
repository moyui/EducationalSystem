from ext import db

# 用户信息


class UserGroup(db.Model):
    __tablename__ = 'usergroup'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))


class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    # 积分
    credit = db.Column(db.BigInteger)
    # 余额
    rest = db.Column(db.Numeric(11, 2))
    # 收益
    income = db.Column(db.Numeric(11, 2))
    phone = db.Column(db.Text)


class UserReport(db.Model):
    __tablename__ = 'userreport'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    content = db.Column(db.Text)
    createdate = db.Column(db.Text)


class UserAppeal(db.Model):
    __tablename__ = 'userappeal'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    content = db.Column(db.Text)
    createdate = db.Column(db.Text)

# 课程信息


class CourseGroup(db.Model):
    __tablename__ = 'coursegroup'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


class CourseVariety(db.Model):
    __tablename__ = 'coursevariety'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    groupid = db.Column(db.Integer, db.ForeignKey('coursegroup.id'))

# 教师信息


class TeacherInfo(db.Model):
    __tablename__ = 'teacherinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    info = db.Column(db.Text)
    favor = db.Column(db.Float)


class ConnectType(db.Model):
    __tablename__ = 'connecttype'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


class TeacherConnect(db.Model):
    __tablename__ = 'teacherconnect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeid = db.Column(db.Integer, db.ForeignKey('connecttype.id'))
    teacherid = db.Column(db.Integer,  db.ForeignKey('teacherinfo.id'))
    value = db.Column(db.Text)


class CourseInfo(db.Model):
    __tablename__ = 'courseinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    info = db.Column(db.Text)
    extrainfo = db.Column(db.Text)
    price = db.Column(db.Numeric(11, 2))
    teacherid = db.Column(db.Integer, db.ForeignKey('teacherinfo.id'))
    # 订阅人数
    buynum = db.Column(db.BigInteger)
    favour = db.Column(db.Float)
    # 课程总共能学多长时间
    courselast = db.Column(db.BigInteger)
    # 列表图片
    mainimg = db.Column(db.Text)


class TagVariety(db.Model):
    __tablename__ = 'tagvariety'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


class CourseTag(db.Model):
    __tablename__ = 'coursetag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    tagid = db.Column(db.Integer, db.ForeignKey('tagvariety.id'))


class CourseClassify(db.Model):
    __tablename__ = 'courseclassify'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    variety = db.Column(db.Integer, db.ForeignKey('coursevariety.id'))

# 开课时间表


class CourseTime(db.Model):
    __tablename__ = 'coursetime'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    time = db.Column(db.Text)


class CourseMenu(db.Model):
    __tablename__ = 'coursemenu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    title = db.Column(db.Text)


class CommentStatus(db.Model):
    __tablename__ = 'commentstatus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


class CourseComment(db.Model):
    __tablename__ = 'coursecomment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    createdate = db.Column(db.Text)
    modifydate = db.Column(db.Text)
    content = db.Column(db.Text)
    coursetime = db.Column(db.Text)
    addcontent = db.Column(db.Text)
    status = db.Column(db.Integer, db.ForeignKey('commentstatus.id'))


class VideoInfo(db.Model):
    __tablename__ = 'videoinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    totaltime = db.Column(db.Text)
    title = db.Column(db.Text)
    url = db.Column(db.Text)
    picurl = db.Column(db.Text)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    menuid = db.Column(db.Integer, db.ForeignKey('coursemenu.id'))


class CourseWareType(db.Model):
    __tablename__ = 'coursewaretype'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)


class CourseWareInfo(db.Model):
    __tablename__ = 'coursewareinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.Text)
    createdate = db.Column(db.Text)
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    typeid = db.Column(db.Integer, db.ForeignKey('coursewaretype.id'))

# 课程测试类型
class TestType(db.Model):
    __tablename__ = 'testtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class CourseTest(db.Model):
    __tablename__ = 'coursetest'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text)
    choice = db.Column(db.Text)
    answer = db.Column(db.Text)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    typeid = db.Column(db.Integer, db.ForeignKey('testtype.id'))
    videoid = db.Column(db.Integer)


class OrderStatus(db.Model):
    __tablename__ = 'orderstatus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))


#  用户成就 
class HonerType(db.Model):
    __tablename__ = 'honertype'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

class UserHoner(db.Model):
    __tablename__ = 'userhoner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    typeid = db.Column(db.Integer, db.ForeignKey('honertype.id'))
    videoid = db.Column(db.Integer)
    createdate = db.Column(db.Text)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))

# 用户课程相关


class UserOrder(db.Model):
    __tablename__ = 'userorder'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    statusid = db.Column(db.Integer, db.ForeignKey('orderstatus.id'))
    createdate = db.Column(db.Text)
    finishdate = db.Column(db.Text)


class AwardType(db.Model):
    __tablename__ = 'awardtype'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    url = db.Column(db.Text)


class UserAward(db.Model):
    __tablename__ = 'useraward'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeid = db.Column(db.Integer, db.ForeignKey('awardtype.id'))
    createdate = db.Column(db.Text)

# 用户扣款表


class UserDeposit(db.Model):
    __tablename__ = 'userdeposit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    amount = db.Column(db.Numeric(11, 2))
    createdate = db.Column(db.Text)
    fromid = db.Column(db.Integer)


# 支付方式


class PayWay(db.Model):
    __tablename__ = 'payway'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

# 用户余额


class RestInfo(db.Model):
    __tablename__ = 'restinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    amount = db.Column(db.Numeric(11, 2))
    createdate = db.Column(db.Text)
    payway = db.Column(db.Integer, db.ForeignKey('payway.id'))
    distribute = db.Column(db.Integer)

# 用户学习进度（对应每个视频）
class UserProgress(db.Model):
    __tablename__ = 'userprogress'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))


# 用户答案表
class UserAnswer(db.Model):
    __tablename__ = 'useranswer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    coursetestid = db.Column(db.Integer, db.ForeignKey('coursetest.id'))
    answer = db.Column(db.Text)
    score = db.Column(db.Text)


# 用户成绩合格记录表
class UserQualify(db.Model):
    __tablename__ = 'userqualify'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    answerid = db.Column(db.Integer, db.ForeignKey('useranswer.id'))
    createdate = db.Column(db.Text)


    # 用户帮助推广机制


class UserDistribution(db.Model):
    __tablename__ = 'userdistribution'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    radio = db.Column(db.Numeric(11, 2))
    link = db.Column(db.Text)
    isopen = db.Column(db.Boolean)


class UserDistributionDetail(db.Model):
    __tablename__ = 'userdistributiondetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distributioniod = db.Column(
        db.Integer, db.ForeignKey('userdistribution.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    income = db.Column(db.Numeric(11, 2))


# 用学习进度表计算
class UserWithDrawMoney(db.Model):
    __tablename__ = 'userwidthdrawal'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    money = db.Column(db.Numeric(11, 2))


class VideoComment(db.Model):
    __tablename__ = 'videocomment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    content = db.Column(db.Text)


class VideoCommentSecond(db.Model):
    __tablename__ = 'videocommentsecond'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    commentid = db.Column(db.Integer, db.ForeignKey('videocomment.id'))
    to = db.Column(db.Integer, db.ForeignKey('userinfo.id'))


class Chat(db.Model):
    __tablename__ = 'chart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    teacherid = db.Column(db.Integer, db.ForeignKey('teacherinfo.id'))
    content = db.Column(db.Text)
    createDate = db.Column(db.Text)

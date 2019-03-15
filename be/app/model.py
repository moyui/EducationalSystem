from ext import db

# 用户信息

class UserGroup(db.Model):
    __tablename__ = 'usergroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    # 积分
    credit = db.Column(db.Integer)
    # 余额
    rest = db.Column(db.Float)
    # 收益
    income = db.Column(db.Float)

# 课程信息


class CourseGroup(db.Model):
    __tablename__ = 'coursegroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


class CourseVariety(db.Model):
    __tablename__ = 'coursevariety'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    groupid = db.Column(db.Integer, db.ForeignKey('coursegroup.id'))


# 课程状态
class CourseStatus(db.Model):
    __tablename__ = 'coursestatus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

# 教师信息


class TeacherInfo(db.Model):
    __tablename__ = 'teacherinfo'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    info = db.Column(db.Text)
    favor = db.Column(db.Float)
    connect = db.Column(db.Text)


class ConnectType(db.Model):
    __tablename__ = 'connecttype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

class TeacherConnect(db.Model):
    __tablename__ = 'teacherconnect'
    id = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer, db.ForeignKey('connecttype.id'))
    teacherid = db.Column(db.Integer,  db.ForeignKey('teacherinfo.id'))
    value = db.Column(db.Text)


class CourseInfo(db.Model):
    __tablename__ = 'courseinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    info = db.Column(db.Text)
    extrainfo = db.Column(db.Text)
    price = db.Column(db.Float)
    tag = db.Column(db.Text)  # 这边其实也要做另外一张表
    teacherid = db.Column(db.Integer, db.ForeignKey('teacherinfo.id'))
    buynum = db.Column(db.Integer)
    favour = db.Column(db.Float)
    # 课程总共能学多长时间
    courselast = db.Column(db.Integer)


class CourseClassify(db.Model):
    __tablename__ = 'courseclassify'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    variteyid = db.Column(db.Integer, db.ForeignKey('coursevariety.id'))

# 开课时间表

class CourseTime(db.Model):
    __tablename__ = 'coursetime'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    time = db.Column(db.String(64))


class CourseMenu(db.Model):
    __tablename__ = 'coursemenu'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    title = db.Column(db.Text)

class CommentStatus(db.Model):
    __tablename__ = 'commentstatus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


class CourseComment(db.Model):
    __tablename__ = 'coursecomment'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    createdate = db.Column(db.String(64))
    content = db.Column(db.Text)
    star = db.Column(db.Integer)
    coursetime = db.Column(db.Integer)
    add = db.Column(db.Boolean)
    addbelongid = db.Column(db.Integer)
    status = db.Column(db.Integer, db.ForeignKey('commentstatus.id'))


class VideoInfo(db.Model):
    __tablename__ = 'videoinfo'
    id = db.Column(db.Integer, primary_key=True)
    totaltime = db.Column(db.Integer)
    title = db.Column(db.Text)
    url = db.Column(db.Text)
    picurl = db.Column(db.Text)
    menuid = db.Column(db.Integer, db.ForeignKey('coursemenu.id'))

class CourseWareType(db.Model):
    __tablename__ = 'coursewaretype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

class CourseWareInfo(db.Model):
    __tablename__ = 'coursewareinfo'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    createdate = db.Column(db.String(64))
    typeid = db.Column(db.Integer)


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    typeid = db.Column(db.Integer)

# 缺少优惠券类型


# 用户课程相关
class UserOrder(db.Model):
    __tablename__ = 'userorder'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    createdate = db.Column(db.String(64))
    finishdate = db.Column(db.String(64))
    lasttime = db.Column(db.Integer)

class AwardType(db.Model):
    __tablename__ = 'awardtype'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    url = db.Column(db.Text)

class UserAward(db.Model):
    __tablename__ = 'useraward'
    id = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer, db.ForeignKey('awardtype.id'))
    createdate = db.Column(db.String(64))


# 用户学习进度（对应每个视频）
class UserProgress(db.Model):
    __tablename__ = 'userprogress'
    id = db.Column(db.Integer, primary_key=True)
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    time = db.Column(db.Integer)

class UserCollect(db.Model):
    __tablename__ = 'usercollect'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))

# 用户扣款
class UserDeposit(db.Model):
    __tablename__ = 'userdeposit'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    amount = db.Column(db.Float)
    createdate = db.Column(db.String(64))

# 用户支付
class UserPayment(db.Model):
    __tablename__ = 'userpayment'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    # 订单号
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    amount = db.Column(db.Float)
    createdate = db.Column(db.String(64))


class CreditWay(db.Model):
    __tablename__ = 'creditway'
    id = db.Column(db.Integer, primary_key=True)
    way = db.Column(db.String(64), unique=True)

class UserCredit(db.Model):
    __tablename__ = 'usercredit'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    wayid = db.Column(db.Integer, db.ForeignKey('creditway.id'))
    amount = db.Column(db.Float)
    createdate = db.Column(db.String(64))

# 用户帮助推广机制
class UserDistribution(db.Model):
    __tablename__ = 'userdistribution'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    radio = db.Column(db.Float)
    link = db.Column(db.Text)

class UserDistributionDetail(db.Model):
    __tablename__ = 'userdistributiondetail'
    id = db.Column(db.Integer, primary_key=True)
    distributioniod = db.Column(db.Integer, db.ForeignKey('userdistribution.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    income = db.Column(db.Float)
    status = db.Column(db.Integer, db.ForeignKey('coursestatus.id'))


# 用学习进度表计算
class UserWithDrawMoney(db.Model):
    __tablename__ = 'userwidthdrawal'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    money = db.Column(db.Float)

class VideoComment(db.Model):
    __tablename__ = 'videocomment'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    content = db.Column(db.Text)

class VideoCommentSecond(db.Model):
    __tablename__ = 'videocommentsecond'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    commentid = db.Column(db.Integer, db.ForeignKey('videocomment.id'))
    to = db.Column(db.Integer, db.ForeignKey('userinfo.id'))

class Chart(db.Model):
    __tablename__ = 'chart'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    teacherid = db.Column(db.Integer, db.ForeignKey('teacherinfo.id'))
    content = db.Column(db.Text)
    createDate = db.Column(db.String(64))
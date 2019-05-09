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
    rest = db.Column(db.Numeric)
    # 收益
    income = db.Column(db.Numeric)

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


# 课程状态
class CourseStatus(db.Model):
    __tablename__ = 'coursestatus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)

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
    price = db.Column(db.Numeric)
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
    typeid = db.Column(db.Integer)


class Coupon(db.Model):
    __tablename__ = 'coupon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    typeid = db.Column(db.Integer)

# 缺少优惠券类型


class OrderStatus(db.Model):
    __tablename__ = 'orderstatus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

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


# 用户学习进度（对应每个视频）
class UserProgress(db.Model):
    __tablename__ = 'userprogress'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    videoid = db.Column(db.Integer, db.ForeignKey('videoinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))


# 用户扣款表


class UserDeposit(db.Model):
    __tablename__ = 'userdeposit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    amount = db.Column(db.Numeric)
    createdate = db.Column(db.Text)
    fromid = db.Column(db.Integer)

# 用户支付


class UserPayment(db.Model):
    __tablename__ = 'userpayment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    # 订单号
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    amount = db.Column(db.Numeric)
    createdate = db.Column(db.Text)

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
    amount = db.Column(db.Numeric)
    createdate = db.Column(db.Text)
    payway = db.Column(db.Integer, db.ForeignKey('payway.id'))
    distribute = db.Column(db.Integer)


class CreditWay(db.Model):
    __tablename__ = 'creditway'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    way = db.Column(db.String(64), unique=True)


class UserCredit(db.Model):
    __tablename__ = 'usercredit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    wayid = db.Column(db.Integer, db.ForeignKey('creditway.id'))
    amount = db.Column(db.BigInteger)
    createdate = db.Column(db.Text)

# 用户帮助推广机制


class UserDistribution(db.Model):
    __tablename__ = 'userdistribution'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    radio = db.Column(db.Numeric)
    link = db.Column(db.Text)


class UserDistributionDetail(db.Model):
    __tablename__ = 'userdistributiondetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distributioniod = db.Column(
        db.Integer, db.ForeignKey('userdistribution.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    income = db.Column(db.Numeric)
    status = db.Column(db.Integer, db.ForeignKey('coursestatus.id'))


# 用学习进度表计算
class UserWithDrawMoney(db.Model):
    __tablename__ = 'userwidthdrawal'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    orderid = db.Column(db.Integer, db.ForeignKey('userorder.id'))
    money = db.Column(db.Numeric)


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

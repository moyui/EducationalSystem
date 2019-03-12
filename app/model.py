from . import db

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

# 课程信息


class CourseGroup(db.Model):
    __tablename__ = 'coursegroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


class CourseVariety(db.Model):
    __tablename__ = 'coursevariety'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    groupid = db.Column(db.Integer, db.ForeignKey('couresegroup.id'))

# 教师信息


class TeacherInfo(db.Model):
    __tablename__ = 'teacherinfo'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    info = db.Column(db.Text)
    favor = db.Column(db.Float)
    connect = db.Column(db.Text)

class CourseInfo(db.Model):
    __tablename__ = 'courseinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Float)
    tag = db.Column(db.Text)
    teacherid = db.Column(db.Integer, db.ForeignKey('teacherinfo.id'))
    buynum = db.Column(db.Integer)
    favour = db.Column(db.Float)


class CourseClassify(db.Model):
    __tablename__ = 'courseclassify'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    variteyid = db.Column(db.Integer, db.ForeignKey('coursevariety.id'))


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


class CourseComment(db.Model):
    __tablename__ = 'coursecomment'
    id = db.Column(db.Integer, primary_key=True)
    courseid = db.Column(db.Integer, db.ForeignKey('courseinfo.id'))
    userid = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    time = db.Column(db.Time)
    content = db.Column(db.Text)
    star = db.Column(db.Integer)
    coursetime = db.Column(db.Integer)
    add = db.Column(db.Boolean)
    addbelongid = db.Column(db.Integer)


class VideoInfo(db.Model):
    __tablename__ = 'videoinfo'
    id = db.Column(db.Integer, primary_key=True)
    totaltime = db.Column(db.Integer)
    title = db.Column(db.Text)
    url = db.Column(db.Text)
    pic = db.Column(db.Text)
    menuid = db.Column(db.Integer, db.ForeignKey('coursemenu.id'))

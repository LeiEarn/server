
from flask_login import  UserMixin, login_user
from server.db import db

# 用户的基本类，分为学生以及组织
# 组织只允许发布任务，学生可以发布和接受任务
# 组织的账号信息与学生应大不同，故最好分开两个表
class User(db.Model, UserMixin):
    __abstract__ = True
    unionid = db.Column(db.Integer, primary_key=True) #微信标识
    name = db.Column(db.String(255)) #名称
    account_id = db.Column(db.Integer, unique=True) #学号/组织号
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    



class Student(User):
    __tablename__ = 'student'
    stu_id = db.Column(db.Integer, unique = True)
    name = db.Column(db.String(255))

    def __init__(self, username,  password, stu_id, name):
        super.__init__(username, password)
        self.stu_id = stu_id
        self.name = name

    def login(self):
        login_user(self)

class Orgnization(User):
    __tablename__ = 'orgnization'
    org_id = db.Column(db.Integer, unique = True)
    name = db.Column(db.String(255))

    def __init__(self, username,  password, org_id, name):
        super.__init__(username, password)
        self.org_id = org_id
        self.name = name

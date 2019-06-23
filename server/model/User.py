__all__ = ['User','UnprovedUser',  'Student', 'Company']


import datetime
import threading
import pymysql
print(__name__)
from ..constants import CONST

from ..db import Database


        

class UserTable(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserTable, "_instance"):
            with UserTable._instance_lock:
                if not hasattr(UserTable, "_instance"):
                    UserTable._instance = object.__new__(cls)
        return UserTable._instance
   
    
    def query_user_unionid(self, unionid=None):
        sql = "SELECT * " \
              "FROM user" \
                  "WHERE wechat_id = {id}".format({'id': unionid})

        row = Database.query(sql=sql, fetchone=True)
        if row is None:
            return row
        else:
            return User(wechat_id=row['wechat_id'],
                                        phone_number=row['phone_number'],
                                        nickname=row['nickname'],
                                        gender=ord(row['gender']),
                                        profile_photo=row['photo'],
                                        intro=row['intro'],
                                        create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                                        isprove=row['isprove'])

    def query_user_userid(self, userid=None):
        sql = "SELECT * " \
              "FROM user" \
                  "WHERE userid = {id}".format({'id': userid})

        row = Database.query(sql=sql, fetchone=True)
        if row is None:
            return row
        else:
            return User(wechat_id=row['wechat_id'],
                                        phone_number=row['phone_number'],
                                        nickname=row['nickname'],
                                        gender=ord(row['gender']),
                                        profile_photo=row['photo'],
                                        intro=row['intro'],
                                        create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                                        isprove=row['isprove'])


    def load_detail_unionid(self, unionid=None, identity=None):
        if id is  None:
            return None
        
        """
        查询identity
        """

        if identity is 'S' :
            """
            身份为学生
            查询student_identity
            """
            print('')
            pass
        

        elif identity is 'C' :
            """
            身份为公司
            查询company_identity

            """
            pass

        
        else:
            """
            身份未知时
            返回未知
            """
            pass
        return ""
    
    def load_detail_userid(self, userid=None, identity = None):
        return ""
        pass
    

    def create_new_user(self, unionid, nickname=None, phone_number=None, gender=None, photo=None):

        # create new instance
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = User(wechat_id=unionid,
                         phone_number=phone_number,
                         nickname=nickname,
                         gender=gender,
                         profile_photo=photo,
                         intro='-',
                         create_date=create_date,
                         isprove=0)
        # write into database
       
        sql = "INSERT INTO user(wechat_id, nickname, phone_number, name ,gender, photo, create_date)" \
              "VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s')" \
              % (unionid, nickname, phone_number, "error_name", gender, photo, create_date)

        Database.execute(sql)
        return user

    def update_info(self, unionid, nickname, phone_number, gender, photo):
         # create new instance
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = User(wechat_id=unionid,
                         phone_number=phone_number,
                         nickname=nickname,
                         gender=gender,
                         profile_photo=photo,
                         intro='-',
                         create_date=create_date,
                         isprove='N')
        # write into database
       
        sql = "INSERT INTO user(wechat_id, nickname, phone_number, name ,gender, photo, create_date)" \
              "VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s')" \
              % (unionid, nickname, phone_number, "error_name", gender, photo, create_date)

        Database.execute(sql)

    def update_detail(self, unionid):
        return ""
        pass


"""

    NU: Unproved 

waiting to be proved
    WS: WAITING S
    WC: WAITING C

proved
    PS: STUDENT
    PC: COMPANY

failing to be proved
    FS:
    FC:
"""


"""
负责根据不同的身份创建对象？
"""
class User(object):
    table = UserTable()

    class BasicUser(object):
        """
        Attributes:
            wechat_id: user's wechat id
            profile_photo: how to load the profile photo?
            nickname: user's nickname, the default value is wechat nickname
            phone_number: user's phone number
            gender: man or female
            intro: introduction
            create_date: date when this user was created
            isprove:    N W F P
            identity:   U S C
        """
        
        __slots__ = ['wechat_id', 'nickname', 'phone_number', 'gender', 'profile_photo', 'intro', 'create_date', 'isprove', 'identity']
        table = UserTable()
        def __init__(self, wechat_id, profile_photo, nickname, phone_number, gender, intro, create_date, isprove='N', identity='U'):
            """
                type is_proved: Datetime
            """
            self.wechat_id = wechat_id
            self.nickname = nickname
            self.phone_number = phone_number
            self.gender = gender
            self.profile_photo = profile_photo
            self.intro = intro
            self.create_date = create_date
            self.isprove = isprove
            self.identity = identity
        def get_type(self):
            return {'iprove': self.isprove, 'identity': self.identity}
    # 未认证
    class UnprovedUser(BasicUser):
        def __init__(self, *args, **kwargs):
            super(AnonymousUser, self).__init__(*args, **kwargs)

    # 学生
    class Student(BasicUser):
        __slots__ = ['college', 'std_id', 'school', 'major']

        def __init__(self,*args, **kwargs):
            super(Student, self).__init__(*args, **kwargs)
            pass
    
    # 公司
    class Company(BasicUser):
        __slots__ = ['company']

        def __init__(self,*args, **kwargs):
            super(Company, self).__init__(*args, **kwargs)
            pass
    


    identity_dict = {'U': UnprovedUser,  'S': Student, 'C': Company}
    def __new__(cls, *args, **kwargs):
        if  'identity' in kwargs:
            identity = kwargs.get('identity')
            user = identity_dict[identity](*args, **kwargs)
            return user
        else:
            identity = 'N'
            user = identity_dict[identity](*args, **kwargs)
            return user


UnprovedUser = User.UnprovedUser
Student = User.Student
Company = User.Company
if __name__ == '__main__':
    #b = BasicUser()
    pass
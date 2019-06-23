__all__ = ['BasicUser', 'AuthenticatedUser', 'Student', 'Company']


import datetime
import threading
import pymysql
print(__name__)
from ..constants import CONST

from ..db import Database

"""
负责根据不同的身份创建对象？
"""
class User(object):
    def __new__(cls, *args, **kwargs):
        if kwargs.get('identity') is not None:
            identity = kwargs.get('identity')
        

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
   


    def query_user(self, id=None):
        sql = "SELECT * " \
              "FROM user" \
                  "WHERE wechat_id = {id}".format({'id': id})

        row = Database.query(sql=sql, fetchone=True)
        if row is None:
            return row
        else:
            return BasicUser(wechat_id=row['wechat_id'],
                                        phone_number=row['phone_number'],
                                        nickname=row['nickname'],
                                        gender=ord(row['gender']),
                                        profile_photo=row['photo'],
                                        intro=row['intro'],
                                        create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                                        isprove=row['isprove'])
        
            

    def create_new_user(self, wechat_id, nickname, phone_number, gender, photo):

        # create new instance
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = BasicUser(wechat_id=wechat_id,
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
              % (wechat_id, nickname, phone_number, "error_name", gender, photo, create_date)

        Database.execute(sql)




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
    """
    __slots__ = ['wechat_id', 'nickname', 'phone_number', 'gender', 'profile_photo', 'intro', 'create_date', 'isprove']
    table = UserTable()
    def __init__(self, wechat_id, profile_photo, nickname, phone_number, gender, intro, create_date, isprove):
        """

        :type is_proved: Datetime
        """
        self.wechat_id = wechat_id
        self.nickname = nickname
        self.phone_number = phone_number
        self.gender = gender
        self.profile_photo = profile_photo
        self.intro = intro
        self.create_date = create_date
        self.isprove = isprove


class AuthenticatedUser(BasicUser):
    """
    Attributes:
        identification: the authentification that had been certified by the administrator
    """
    __slots__ = ['identification']

    def __init__(self):
        super(AuthenticatedUser, self).__init__()
        pass


class Student(AuthenticatedUser):
    __slots__ = ['college', 'std_id', 'school', 'major']

    def __init__(self):
        super(Student, self).__init__()
        pass


class Company(AuthenticatedUser):
    __slots__ = ['company']

    def __init__(self):
        super(Company, self).__init__()
        pass


if __name__ == '__main__':
    #b = BasicUser()
    pass
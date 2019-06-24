
import datetime
import threading
import pymysql
print(__name__)
from ..constants import CONST

from ..utils.db import Database


        

class UserTable(object):
    _instance_lock = threading.Lock()

    user_table = "user"
    stu_identity = "stu_identity"
    com_identity = "com_identity"
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserTable, "_instance"):
            with UserTable._instance_lock:
                if not hasattr(UserTable, "_instance"):
                    UserTable._instance = object.__new__(cls)
        return UserTable._instance

    def query_user(self, unionid=None, user_id=None):
        """
            query_user by user_id or unionid

        """
        if unionid is not None:
            sql = "SELECT *  \
                  FROM user \
                      WHERE wechat_id = {id}".format(id = unionid)
        else:
            sql =  "SELECT *  \
                  FROM user \
                      WHERE user_id = {id}".format(id = user_id)
        row = Database.query(sql=sql, fetchone=True)
        if row is None:
            return row
        else:
            return User(
                user_id = row['user_id'],
                wechat_id=row['wechat_id'],
                nickname=row['nickname'],
                phone_number=row['phone_number'],
                photo=row['photo'],
                identity=row['identity'],
                intro=row['intro'],
                create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                isprove=row['isprove'])

    def load_detail_user_id(self, user_id=None, identity=None):
        """
           load_detailby user_id or unionid

        """
        if user_id is  None:
            return None
        """
        查询identity
        """

        if identity is 'S' :
            """
            身份为学生
            查询student_identity
            """
            sql =  "SELECT * " \
              "FROM stu_identity" \
                  "WHERE user_id = {id}".format(id = user_id)

        elif identity is 'C' :
            """
            身份为公司
            查询company_identity

            """
            sql =  "SELECT * " \
              "FROM com_identity" \
                  "WHERE user_id = {id}".format(id = user_id)
        else:
            """
            身份未知时
            返回未知
            """
            return ""

        result =Database.query(sql, fetchone=True)
        return result

    def create_new_user(self, unionid, nickname=None, phone_number=None, gender=None, photo=None):

        # create new instance
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = User(wechat_id=unionid,
                         phone_number=phone_number,
                         nickname=nickname,
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

    def update_info(self, unionid, **kwargs):
        """
        根据参数的属性，更改 user_id 对应的user 的属性
        args:
            nickname, phone_number, gender, photo
        example:
            update_user(user_id=1, audit_id=1, type = 1)
        """
        sql = "UPDATE user \
            SET "
        for key, value in kwargs.items():
            if key in User.BasicUser.__slots__:
                sql += " {key} = {value} ".format(key = key, value= value)

        sql += "WHERE unionid = {unionid}".format(unionid=unionid)

        result = Database.execute(sql, response = True)

        query_sql = "SELECT * FROM user WHERE unionid = {unionid}".format(unionid=unionid)
        user = Database.query(query_sql, fetchone=True)
        return user

    def prove(self, user_id ):
        pass

    def update_detail(self, unionid, identity, **kwargs):
        """
        根据参数的属性，更改 user_id 对应的identity 的属性
        args:
            nickname, phone_number, gender, photo
        example:
            update_user(user_id=1, audit_id=1, type = 1)
        """
        if identity is 'S':
            sql =  "UPDATE {stu_identity} \
            SET ".format(UserTable.stu_identity)
            for key, value in kwargs.items():
                if key in User.Student.__slots__:
                    sql += " {key} = {value} ".format(key = key, value= value)
        elif identity is 'C':
            sql = "UPDATE {com_identity} \
                SET ".format(UserTable.com_identity)
            for key, value in kwargs.items():
                if key in User.Company.__slots__:
                    sql += " {key} = {value} ".format(key = key, value= value)


        sql += "WHERE unionid = {unionid}".format(unionid=unionid)

        result = Database.execute(sql, response = True)

        query_sql = "SELECT * FROM user WHERE unionid = {unionid}".format(unionid = unionid)
        user = Database.query(query_sql, fetchone=True)
        return user

    @staticmethod
    def user_count(user_type='all'):
        if user_type == 'all':
            sql = 'SELECT COUNT(*) as count FROM user;'
        elif user_type == 'waiting':
            sql = 'SELECT COUNT(*) FROM user WHERE user.isprove = FALSE;'
        else:
            raise KeyError

        return Database.execute(sql, response=True)[0]['count']


    @staticmethod
    def get_users(user_type='all', begin=0, end=100):
        sql = 'SELECT * FROM user LIMIT %d OFFSET %d;' % (end - begin, begin)

        return Database.execute(sql, response=True)


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
            user_id: user's id
            wechat_id: user's wechat id
            profile_photo: how to load the profile photo?
            nickname: user's nickname, the default value is wechat nickname
            phone_number: user's phone number
            intro: introduction
            create_date: date when this user was created
            isprove:    N W F P
            identity:   U S C
        """

        __slots__ = ['wechat_id', 'nickname', 'phone_number', 'profile_photo', 'intro', 'create_date', 'isprove', 'identity']
        table = UserTable()
        def __init__(self, **kwargs):
            """
                type is_proved: Datetime
            """
            for key, value in list(kwargs.items()):
                if key in self.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)
            if self.__getattribute__('isprove') is None:
                self.isprove = kwargs.get('isprove')
            if self.__getattribute__('identity') is None:
                self.identity = kwargs.get('identity')
        def get_type(self):
            return {'iprove': self.isprove, 'identity': self.identity}
    # 未认证
    class UnprovedUser(BasicUser):
        def __init__(self, *args, **kwargs):
            super(UnprovedUser, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in self.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)


    # 学生
    class Student(BasicUser):
        __slots__ = ['college', 'stu_num', 'school',  'name', 'phone_number', 'email', 'gender','prove', 'prove_state']

        def __init__(self,*args, **kwargs):
            super(Student, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in self.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)

    # 公司
    class Company(BasicUser):
        __slots__ = ['company',  'name', 'phone_number', 'email','prove', 'prove_state']

        def __init__(self,*args, **kwargs):
            super(Company, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in self.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)



    identity_dict = {'U': UnprovedUser,  'S': Student, 'C': Company}
    def __new__(cls, *args, **kwargs):
        if  'identity' in kwargs:
            identity = kwargs.get('identity')
            user = cls.identity_dict[identity](*args, **kwargs)
            return user
        else:
            identity = 'U'
            user = cls.identity_dict[identity](*args, **kwargs)
            return user




UnprovedUser = User.UnprovedUser
Student = User.Student
Company = User.Company
if __name__ == '__main__':
    #b = BasicUser()
    pass
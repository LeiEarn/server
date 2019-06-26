# -*- coding: utf-8 -*-
__all__ = ['User', 'UnprovedUser',  'Student', 'Company']



import datetime
import threading
import pymysql
print(__name__)

from ...utils.db import Database


        

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
            sql = "SELECT * " \
                    "FROM user "\
                    "WHERE wechat_id = '{id}'".format(id = unionid)
        else:
            sql =  "SELECT * " \
                    " FROM user "\
                    " WHERE user_id = '{id}'".format(id = user_id)
        row = Database.query(sql=sql, fetchone=True)
        if row is None:
            return row
        else:
            return User(
                user_id = row['user_id'],
                wechat_id=row['wechat_id'],
                nickname=row['nickname'],
                photo=row['photo'],
                identity=row['identity'],
                intro=row['intro'],
                create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                isprove=row['isprove'])
    
    def get_user_info(self, user_id):
        sql =  "SELECT * " \
                    " FROM user "\
                    " WHERE user_id = '{id}'".format(id = user_id)
        row = Database.query(sql=sql, fetchone=True)
        
        return row

    def load_detail_user_id(self, user_id=None, identity=None):
        """
           load_detailby user_id or unionid

        """
        if user_id is  None:
            return None
        """
        查询identity
        """
        print(identity)
        if identity is 'S' :
            """
            身份为学生
            查询student_identity
            """
            sql =  "SELECT * FROM stu_identity WHERE user_user_id = '{id}'".format(id = user_id)

        elif identity is 'C' :
            """
            身份为公司
            查询company_identity

            """
            sql =  "SELECT * FROM com_identity WHERE user_user_id = '{id}'".format(id = user_id)
        else:
            """
            身份未知时
            返回未知
            """
            return {}
        print(sql)
        result = Database.query(sql, fetchone=True)
        return result

    def create_new_user(self, unionid, nickname='nick', photo=''):
        identity='U'
        isprove='N'
        intro = '-'
        credit=100
        balance=0
        # create new instance
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = User(wechat_id=unionid,
                         nickname=nickname,
                         profile_photo=photo,
                         intro=intro,
                         create_date=create_date,
                         identity=identity,
                         isprove=isprove)
        # write into database
       
        sql = "INSERT INTO user(wechat_id, nickname ,identity, isprove, photo,intro, create_date, credit, balance) \
              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (unionid, nickname,identity, isprove, photo, intro, create_date, credit, balance)

        Database.execute(sql)
        return user

    def update_info(self, unionid, **kwargs):
        """
        根据参数的属性，更改 user_id 对应的user 的属性
        args:
            nickname, gender, photo
        example:
            update_user(user_id=1, audit_id=1, type = 1)
        """
        sql = "UPDATE user \
            SET "
        
        for key, value in kwargs.items():
            if key in User.BasicUser.__slots__:
                sql += " {key} = '{value}',".format(key = key, value= value)
        sql = sql[:-1]
        sql += "  WHERE wechat_id = '{unionid}'".format(unionid=unionid)
        print(sql)
        result = Database.execute(sql, response = True)

        query_sql = "SELECT * FROM user WHERE wechat_id = '{unionid}'".format(unionid=unionid)
        user = Database.query(query_sql, fetchone=True)
        return user

    def prove(self, user_id, identity, name,gender,phone_number,prove='no materials', school=None,company=None, id=None ):
        state_prove = 'W'
        email = " "
        college = ""
        user_user_id = user_id
        if identity is 'S':
            student_num = id

            info = self.load_detail_user_id(user_id = user_id, identity = identity)
            if info is None:
                sql = "INSERT INTO {stu_identity}(college, school,  name, phone_number,student_num, email, gender,prove, state_prove, user_user_id)\
                    VALUES ('{college}', '{school}', '{name}', '{phone_number}', '{student_num}', '{email}', '{gender}', '{prove}', '{state_prove}', '{user_user_id}')"\
                        "".format(
                                stu_identity = self.stu_identity,
                                college=college, school=school, name=name, 
                                phone_number=phone_number, student_num=student_num, 
                                email=email, gender=gender, prove=prove, state_prove=state_prove, user_user_id=user_user_id)
            else:
                sql = "UPDATE {stu_identity}"\
                " SET college='{college}', school='{school}', name='{name}', "\
                    "phone_number='{phone_number}', student_num='{student_num}', "\
                        "email='{email}', gender='{gender}', prove='{prove}', state_prove='{state_prove}', user_user_id='{user_user_id}'"\
                            "".format(
                                stu_identity = self.stu_identity,
                                college=college, school=school, name=name, 
                                phone_number=phone_number, student_num=student_num, 
                                email=email, gender=gender, prove=prove, state_prove=state_prove, user_user_id=user_user_id)
        elif identity is 'C':
            job_num = id
            info = self.load_detail_user_id(user_id = user_id, identity = identity)
            if info is None:
                sql = "INSERT INTO {com_identity}(company,  name, phone_number,job_num, email, gender,prove, state_prove, user_user_id)"\
                    " VALUES ('{company}', '{name}', '{phone_number}', '{job_num}', '{email}', '{gender}', '{prove}', '{state_prove}', '{user_user_id}')"\
                         "".format(
                                com_identity=self.com_identity,
                                company=company,  name=name, 
                                phone_number=phone_number, job_num=job_num, 
                                email=email, gender=gender, prove=prove, state_prove=state_prove, user_user_id=user_user_id)
            else:
                sql = "UPDATE {com_identity}"\
                " SET company='{company}',  name='{name}', "\
                    "phone_number='{phone_number}', job_num='{job_num}', "\
                        "email='{email}', gender='{gender}', prove='{prove}', state_prove='{state_prove}', user_user_id='{user_user_id}'"\
                            "".format(
                                com_identity=self.com_identity,
                                company=company,  name=name, 
                                phone_number=phone_number, job_num=job_num, 
                                email=email, gender=gender, prove=prove, state_prove=state_prove, user_user_id=user_user_id)
        result = Database.execute(sql)
        return result

    def update_detail(self, user_id,identity, **kwargs):
        """
        根据参数的属性，更改 user_id 对应的identity 的属性
        args:
            nickname, phone_number, gender, photo
        example:
            update_user(user_id=1, audit_id=1, type = 1)
        """
        if identity is 'S':
            sql =  "UPDATE {stu_identity} \
            SET ".format(stu_identity = UserTable.stu_identity)
            for key, value in kwargs.items():
                if key in User.Student.__slots__:
                    if type(value) is str:
                        sql += " {key} = '{value}',".format(key = key, value= value)
                    else:

                        sql += " {key} = '{value}',".format(key = key, value= value)
        elif identity is 'C':
            sql = "UPDATE {com_identity} \
                SET ".format(UserTable.com_identity)
            for key, value in kwargs.items():
                if key in User.Company.__slots__:
                    sql += " {key} = '{value}',".format(key = key, value= value)

        sql = sql[:-1]
        sql += " WHERE user_user_id = '{user_id}'".format(user_id=user_id)

        result = Database.execute(sql, response = True)

        query_sql = "SELECT * FROM user WHERE user_id = '{user_id}'".format(user_id = user_id)
        user = Database.query(query_sql, fetchone=True)
        return user

    @staticmethod
    def user_count(user_type='all'):
        if user_type == 'all':
            sql = 'SELECT COUNT(*) as count FROM user;'
        elif user_type == 'waiting':
            sql = 'SELECT COUNT(*) as count FROM user WHERE user.isprove=\'W\';'
        else:
            raise KeyError

        return Database.execute(sql, response=True)[0]['count']

    @staticmethod
    def specific_user_count(gender='all', identity='S'):
        sql = 'SELECT COUNT(*) as count '\
            + 'FROM {} as user '.format('stu_identity' if identity=='S' else 'com_identity') \
            + 'WHERE user.gender=\'{}\''.format(gender)
        print(sql)

        data = Database.query(sql)
        if isinstance(data, Exception):
            return False, data
        else:
            return True, data[0]['count']
    @staticmethod
    def get_users(user_type='all', begin=0, end=100):
        if user_type == 'all':
            sql = 'SELECT * FROM user LIMIT %d OFFSET %d;' % (end - begin, begin)
        elif user_type == 'waiting':
            sql = 'SELECT * FROM user WHERE user.isprove=\'W\' LIMIT %d OFFSET %d;' % (end - begin, begin)
        else:
            raise KeyError('wrong user type %s' % user_type)
        result = Database.execute(sql, response=True)
        for user in result:
            user['create_date'] = str(user['create_date'])
        return result

    @staticmethod
    def audit(user_id, identity, audit):
        audit = 'P' if audit else 'F'
        sql = 'UPDATE user SET user.isprove=\'%s\' WHERE user.user_id = %d;' % (audit, user_id)
        sql_ = 'UPDATE %s SET state_prove=\'%s\' WHERE user_user_id = %d;' % \
               ('com_identity' if identity == 'C' else 'stu_identity', audit, user_id)
        print(sql,sql_)
        try:
            connect = Database.get_conn()
            with connect.cursor() as cursor:
                cursor.execute(sql)
                cursor.execute(sql_)
            connect.commit()

            return (True, 'success audit')
        except Exception as e:
            print(e)
            connect.rollback()
            return (False, 'Database execute error : %s' %e)

    @staticmethod
    def get_school_count():
        sql = 'SELECT school, COUNT(*) as count FROM stu_identity GROUP BY school;'
        print(sql)
        return Database.query(sql)

    @staticmethod
    def get_company_count():
        sql = 'SELECT name, COUNT(*) as count FROM com_identity GROUP BY name;'
        print(sql)
        return Database.query(sql)


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
            intro: introduction
            create_date: date when this user was created
            isprove:    N W F P
            identity:   U S C
        """

        __slots__ = ['user_id', 'wechat_id', 'nickname', 'photo', 'intro', 'create_date', 'isprove', 'identity', 'balance', 'credit']
        table = UserTable()
        def __init__(self, **kwargs):
            """
                type is_proved: Datetime
            """
            for key, value in list(kwargs.items()):
                if key in User.BasicUser.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)
            if not hasattr(self, 'isprove') :
                self.isprove = kwargs.get('isprove')
            if not hasattr(self, 'identity') :
                self.identity = kwargs.get('identity')

        def get_type(self):
            return {'isprove': self.isprove, 'identity': self.identity}

        def info_basic_dict(self):
            return { key:self.__getattribute__(key) for key in User.BasicUser.__slots__}


    # 未认证
    class UnprovedUser(BasicUser):
        def __init__(self, *args, **kwargs):
            super(UnprovedUser, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in User.UnprovedUser.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)

    # 学生
    class Student(BasicUser):
        __slots__ = ['college', 'user_stu_id', 'school',  'name', 'phone_number','student_num', 'email', 'gender','prove', 'state_prove']

        def __init__(self,*args, **kwargs):
            super(Student, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in User.Student.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)

    # 公司
    class Company(BasicUser):
        __slots__ = ['company', 'user_com_id', 'job_num','name', 'gender', 'phone_number', 'email','prove', 'state_prove']

        def __init__(self,*args, **kwargs):
            super(Company, self).__init__(*args, **kwargs)
            for key, value in list(kwargs.items()):
                if key in User.Company.__slots__:
                    self.__setattr__(key, value)
                    kwargs.pop(key)


    isprove_list = ['N','W','F','P' ]
    identity_dict = {'U': UnprovedUser,  'S': Student, 'C': Company}

    def __new__(cls, *args, **kwargs):

        if 'isprove' in kwargs:
            if kwargs.get('isprove') not in cls.isprove_list:
                kwargs['isprove'] = 'N'
        if  'identity' in kwargs:
            identity = kwargs.get('identity')
            if identity not in cls.identity_dict:
                kwargs['identity'] = 'U'
                identity = 'U'
            user = cls.identity_dict[identity](*args, **kwargs)
            return user
        else:
            kwargs['identity'] = 'U'
            identity = 'U'
            user = cls.identity_dict[identity](*args, **kwargs)
            return user


UnprovedUser = User.UnprovedUser
Student = User.Student
Company = User.Company
if __name__ == '__main__':
    #b = BasicUser()
    pass

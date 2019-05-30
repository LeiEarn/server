from model import *
import datetime
import threading
import pymysql
from constants import CONST

from .db import Database

db = Database()

class UserManagement(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.users = []

    def __new__(cls, *args, **kwargs):
        if not hasattr(UserManagement, "_instance"):
            with UserManagement._instance_lock:
                if not hasattr(UserManagement, "_instance"):
                    UserManagement._instance = object.__new__(cls)
        return UserManagement._instance

    def load_users(self):
        conn = pymysql.connect(host=CONST.HOST,
                               user=CONST.USER,
                               password=CONST.PASSWD,
                               db=CONST.DB,
                               use_unicode=True,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()

        sql = "SELECT *" \
              "FROM user"

        cursor.execute(sql)

        for row in cursor.fetchall():
            self.users.append(BasicUser(wechat_id=row['wechat_id'],
                                        phone_number=row['phone_number'],
                                        nickname=row['nickname'],
                                        gender=ord(row['gender']),
                                        profile_photo=row['photo'],
                                        intro=row['intro'],
                                        create_date=row['create_date'].strftime('%Y-%m-%d %H:%M:%S'),
                                        isprove=row['isprove']))
        # for user in self.users:
        #     print(user.wechat_id,
        #           user.nickname,
        #           user.phone_number,
        #           user.gender,
        #           user.profile_photo,
        #           user.intro,
        #           user.create_date,
        #           user.isprove)
        
    @db.sql_wrapper
    def query_user(self, id=None):
        pass
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

        self.users.append(user)
        # write into database
        conn = pymysql.connect(host=CONST.HOST,
                               user=CONST.USER,
                               password=CONST.PASSWD,
                               db=CONST.DB,
                               use_unicode=True,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        sql = "INSERT INTO user(wechat_id, nickname, phone_number, name ,gender, photo, create_date)" \
              "VALUES ('%s', '%s', '%s', '%s', %d, '%s', '%s')" \
              % (wechat_id, nickname, phone_number, "error_name", gender, photo, create_date)

        cursor.execute(sql)

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    UserManagement = UserManagement()

    UserManagement.load_users()

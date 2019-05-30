import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
import pymysql


import pymysql

class Database(object):
    def __init__(self):
        self.get_conn()
    def init_db(self):
        """Clear existing data and create new tables."""
        db = self.get_conn()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
    def get_conn(self):
        try:
            self.a = 1
            self.conn = pymysql.connect(host=CONST.HOST,
                                user=CONST.USER,
                                password=CONST.PASSWD,
                                db=CONST.DB,
                                use_unicode=True,
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)
            return self.conn
        except pymysql.Error as e:
            print(e)
        
 
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e)
 
    def sql_wrapper(self, fun):
        def run(self, *args,**kwargs):
            db = self.get_conn()
            cursor = db.cursor()
            try:
                cursor.execute(fun(*args,**kwargs))
                li=cursor.fetchall()
                db.commit() 
            except Exception as e: #如果出现错误，回滚事务
                db.rollback() #打印报错信息
                print('运行',str(fun),'方法时出现错误，错误代码：',e)
            finally: #关闭游标和数据库连接
                cursor.close() 
                db.close() 
            try: #返回sql执行信息
                return list(li) 
            except: 
                print('没有得到返回值，请检查代码，该信息出现在ConDb类中的装饰器方法') 
        return run

 
def main():
    db = Database()
    # sql.get_more(3,2)
 
if __name__ == '__main__':
    main()




"""
@click.command('init-db')
@with_appcontext
def init_db_command():
    \"""Clear existing data and create new tables.\"""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    \"""Register database functions with the Flask app. This is called by
    the application factory.
    \"""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

"""
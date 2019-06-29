import sqlite3

from flask import current_app
import pymysql

from ..config import CONST


class Database:
    host = CONST.HOST
    user = CONST.USER
    password = CONST.PASSWD
    db = CONST.DB
    port = CONST.PORT
    charset = "utf8"
    cursorclass = pymysql.cursors.DictCursor
    conn = None

    @classmethod
    def get_conn(cls):
        try:
            cls.conn = pymysql.connect(
                host=CONST.HOST,
                user=CONST.USER,
                password=CONST.PASSWD,
                db=CONST.DB,
                use_unicode=True,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor,
            )
            return cls.conn
        except pymysql.Error as e:
            print("get database error")
            print(repr(e))
            print(e)

    @classmethod
    def close_conn(cls):
        try:
            if cls.conn:
                cls.conn.close()
        except pymysql.Error as e:
            print("close database error")
            print(repr(e))
            print(e)

    @classmethod
    def init_db(cls):
        """Clear existing data and create new tables."""
        db = cls.get_conn()
        result = cls.query("SELECT * FROM user", fetchone=True)
        cls.close_conn()
        """
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        """

    @classmethod
    def query(cls, sql, args=None, fetchone=False):
        # 创建连接
        connection = pymysql.connect(
            host=cls.host,
            port=cls.port,
            user=cls.user,
            password=cls.password,
            db=cls.db,
            use_unicode=True,
            charset=cls.charset,
            cursorclass=cls.cursorclass,
        )
        try:
            result = None
            # 开启游标
            with connection.cursor() as cursor:
                # 返回响应结果数
                print(sql)
                sql_string = cls.sql_args_2_sql(sql, args)
                effect_row = cursor.execute(sql_string)
                if fetchone:
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            # 关闭连接
            connection.close()

        return result

    @classmethod
    def execute(cls, sql, args=None, response=False):
        connection = pymysql.connect(
            host=cls.host,
            user=cls.user,
            port=cls.port,
            password=cls.password,
            db=cls.db,
            use_unicode=True,
            charset=cls.charset,
            cursorclass=cls.cursorclass,
        )

        try:
            result = None
            with connection.cursor() as cursor:
                print(sql)
                effect_row = cursor.execute(cls.sql_args_2_sql(sql, args))
                if response:
                    result = cursor.fetchall()

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        except Exception as e:
            print(e)
            # error rollback
            connection.rollback()
            result = e
        finally:
            connection.close()

        if response:
            return result

    @staticmethod
    def sql_args_2_sql(sql, args):
        """
        fix  issue  %d format: a number is required, not str
        :param sql: sql语句
        :param args: 格式化参数
        :return: 组合之后的sql语句
        """
        if args is None:
            return sql
        if sql.find("%") > -1:
            return sql % args
        elif sql.find("{") > -1:
            if type(args) is dict:
                return sql.format(**args)
            else:
                return sql.format(*args)
        return sql


def main():
    db = Database()
    # sql.get_more(3,2)


if __name__ == "__main__":
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

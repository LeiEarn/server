# -*- coding: utf-8 -*-
import threading

import datetime
from ...utils.db import Database

print(__name__)



class TaskTable(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(TaskTable, "_instance"):
            with TaskTable._instance_lock:
                if not hasattr(TaskTable, "_instance"):
                    TaskTable._instance = object.__new__(cls)
        return TaskTable._instance

    @staticmethod
    def create_task(**kwargs):
        """
        :param kwargs: {
                 'title',
                 'type_',
                 'publish_id',
                 'wjx_id',
                 'task_intro',
                 'max_num',
                 'participants_num',
                 'money',
                 'sign_start_time',
                 'sign_end_time',
                 'audit_administrator_audit_id'
        }
        """
        values = kwargs.update(
            {"release_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
             "state": "W",  # waiting
             "audit_administrator_audit_id": '00227'
             })

        sql = "INSERT INTO task(title, type_, publish_id, state, wjx_id, task_intro, max_num, participants_num, money," \
              "release_time, sign_start_time, sign_end_time, audit_administrator_audit_id)" \
              "VALUES ({title}, {type_}, {publish_id}, {state}, {wjx_id}, {task_intro}, {max_num}, {participants_num}, " \
              "{money}, {release_time}, {sign_start_time}, {sign_end_time}, {audit_administrator_audit_id});"\
            .format(values)
        Database.execute(sql)

    @staticmethod
    def get_task_info(task_id):
        sql = 'SELECT * FROM task WHERE task.task_id=%d;' % (task_id)
        result = Database.execute(sql, response=True)
        return result

    @staticmethod
    def get_accepted_task(user_id):
        sql = "SELECT * FROM user_has_task WHERE user_id = {user_id}".format(user_id=user_id)
        result = Database.execute(sql, response=True)
        return result


    def abort_task(self, task_id):
        return ""

    def add_task_info(self):
        pass

    def commit_job(self, user_id, task_id):
        return ""

    def update_task(self, task_id,  **kwargs):
        """
        根据参数的属性，更改 task_id 对应的task 的属性
        example:
            update_task(task_id=1, audit_id=1, type = 1)
        """
        sql = "UPDATE task SET "
        for key in kwargs:
            if key in Task.__slots__:
                sql += " {key} = {value} ".format(key = key, value= kwargs[key])

        sql += "WHERE task_id = {task_id}".format(task_id=task_id)

        Database.execute(sql)

    def accept_task(self, user_id, task_id):
        return ""

    def abondon_task(self, user_id, task_id):
        return ""

    def updata_status(self):
        pass

    @staticmethod
    def task_count(task_type='all'):
        if task_type == 'all':
            sql = 'SELECT COUNT(*) as count FROM task;'
        elif task_type == 'waiting':
            sql = 'SELECT COUNT(*) as count FROM task WHERE task.state=W;'
        else:
            raise KeyError('task type error')

        return Database.execute(sql, response=True)[0]['count']

    @staticmethod
    def get_tasks(task_type='all', begin=0, end=100):
        if task_type == 'all':
            sql = 'SELECT * FROM task LIMIT %d OFFSET %d;' % (end - begin, begin)
        elif task_type == 'waiting':
            sql = 'SELECT * FROM task WHERE task.state=W LIMIT %d OFFSET %d;' % (end - begin, begin)
        else:
            raise KeyError('task type error')

        result = Database.query(sql)
        for user in result:
            user['release_time'] = str(user['release_time'])
            user['sign_start_time'] = str(user['sign_start_time'])
            user['sign_end_time'] = str(user['sign_end_time'])

        return result

    def get_task_basic_inverse(self, page_id, size):
        start = page_id * size
        end = start + size
        
        sql = " SELECT task.money,task.task_id,task.title, task_intro,task.max_num, participants_num, user.photo as icon "\
            " FROM task,user "\
            " WHERE  user.user_id = task.publish_id ORDER BY task.task_id DESC limit {start}, {end} "\
                .format(start = start, end=end)
        
        result = Database.query(sql)
        for user in result:
            user['create_data'] = str(user['create_data'])

        return result



class Task(object):
    """
    W - waiting
    F - failed
    S - succeed
    B - begin
    E - end
    """
    __slots__ = ['task_id',
                 'title',
                 'type_',
                 'publish_id',
                 'state',
                 'wjx_id',
                 'task_intro',
                 'max_num',
                 'participants_num',
                 'money',
                 'release_time',
                 'sign_start_time',
                 'sign_end_time',
                 'audit_administrator_audit_id'
                 ]
    taskTable = TaskTable()

    def __init__(self, task_id, title, type_, publish_id, state, wjx_id, task_intro, max_num, participants_num, money,
                 release_time, sign_start_time, sign_end_time, audit_administrator_audit_id):
        """
        :param task_id:
        :param title:
        :param type_:
        :param publish_id:
        :param state:
        :param wjx_id:
        :param task_intro:
        :param max_num:
        :param participants_num:
        :param money:
        :param release_time:
        :param sign_start_time:
        :param sign_end_time:
        :param audit_administrator_audit_id:
        """
        self.task_id = task_id
        self.title = title
        self.type_ = type_
        self.publish_id = publish_id
        self.state = state
        self.wjx_id = wjx_id
        self.task_intro = task_intro
        self.max_num = max_num
        self.participants_num = participants_num
        self.money = money
        self.release_time = release_time
        self.sign_start_time = sign_start_time
        self.sign_end_time = sign_end_time
        self.audit_administrator_audit_id = audit_administrator_audit_id


if __name__ =='__main__':

    print(Task.taskTable.task_count())
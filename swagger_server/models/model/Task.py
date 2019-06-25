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
        "title":,
        "type":
        "wjx_id":
        "task_intro":
        "participants_num":
        "sign_start_time":
        "sign_end_time":
        }
        """
        values = kwargs.update({"release_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                       "state": "W",# waiting
                       "audit_administrator_audit_id": '00227'
                       })

        sql = "INSERT INTO task(title, type, state, wjx_id, task_intro, participants_num, release_time, sign_start_time, " \
              "sign_end_time, audit_administrator_audit_id) " \
              "VALUES ({title}, {type}, {state}, {wjx_id}, {task_intro}, {participants_num}, {release_time}," \
              " {sign_start_time}, {sign_end_time}, {audit_administrator_audit_id});"\
            .format(values)
        Database.execute(sql)

    @staticmethod
    def get_task_info(task_id):
        sql = 'SELECT * FROM task WHERE task.task_id=%d;' % (task_id)
        result = Database.execute(sql)
        return result

    def get_accepted_task(self, user_id):
        sql = "SELECT * FROM user_has_task\
            WHERE user_id = {user_id}".format(user_id=user_id)
        result = Database.execute(sql)
        return result


    def abort_task(self, task_id):
        return ""

    def add_task_info(self):
        pass
    def commit_job(self, user_id, task_id):
        return ""
    ####
    def update_task(self, task_id,  **kwargs):
        """
        根据参数的属性，更改 task_id 对应的task 的属性
        example:
            update_task(task_id=1, audit_id=1, type = 1)
        """
        sql = "UPDATE task \
            SET "
        for key in kwargs:
            if key in Task.__slots__:
                sql += " {key} = {value} ".format(key = key, value= kwargs[key])

        sql += "WHERE task_id = {task_id}".format(task_id=task_id)

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

        result = Database.execute(sql, response=True)
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
    __slots__ = ['task_id', 'type', 'intro', 'release_time', 'ss_time', 'se_time', 'ts_time', 'te_time', 'audit_id',
                 'participants_num', 'publisher_id', 'status']
    taskTable = TaskTable()

    def __init__(self, task_id, type, intro, release_time, ss_time, se_time, ts_time, te_time, audit_id, publisher_id):
        """
        :param task_id: Task id, auto_increase
        :param type: Task type(...)
        :param intro: introduction
        :param release_time: Release time
        :param ss_time: sign start time
        :param se_time: sign end time
        :param ts_time: task start time
        :param te_time: task end time
        :param audit_id: Audit adminstrator id
        :param participants_num: number of participants
        :param publisher_id: ..
        """
        self.task_id = task_id
        self.type = type
        self.intro = intro
        self.release_time = release_time
        self.ss_time = ss_time
        self.se_time = se_time
        self.ts_time = ts_time
        self.te_time = te_time
        self.audit_id = audit_id
        self.publisher_id = publisher_id
        self.participants_num = 0
        self.status = 'waitreview'

    def get_info(self):
        return [self.task_id, self.type, self.intro, self.release_time, self.ss_time, self.se_time, self.ts_time,
                self.te_time, self.audit_id, self.publisher_id, self.participants_num]

if __name__ =='__main__':

    print(Task.taskTable.task_count())

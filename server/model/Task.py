import threading
import datetime
from ..db import Database

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

    def create_Task(self, task):
        create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO task(task_id, type, task_intro, participants_num, release_time, sign_start_time, " \
              "sign_end_time, task_start_time, task_end_time, audit_administrator_audit_id) " \
              "VALUES (%s)" % ', '.join(map(str, task.get_info()))
        Database.execute(sql)

        # ??? how to get the task_id?
        return task

    def query_task(self):
        pass

    def updata_status(self):
        pass

class Task(object):
    __slots__ = ['task_id', 'type', 'intro', 'release_time', 'ss_time', 'se_time', 'ts_time', 'te_time', 'audit_id',
                 'participants_num', 'publisher_id', 'status']
    TaskTable = TaskTable()

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
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task = Task(1, 'type', now, 'release', now, now, now, 999, 222, 0)
    print(', '.join(map(str, task.get_info())))
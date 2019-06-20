import threading
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
        # write into database
        pass

    def query_task(self):
        pass

class Task(object):
    __slots__ = ['task_id', 'type', 'intro', 'release_time', 'ss_time', 'se_time', 'ts_time', 'te_time', 'audit_id',
                 'participants_num', 'publisher_id']
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
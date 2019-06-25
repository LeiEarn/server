# -*- coding: utf-8 -*-
import threading
from ..utils.db import Database

class AdminPlatform():
    _instance_lock = threading.Lock()

    __slots__ = ['Task_wait_list']

    def __new__(cls, *args, **kwargs):
        if not hasattr(AdminPlatform, "_instance"):
            with AdminPlatform._instance_lock:
                if not hasattr(AdminPlatform, "_instance"):
                    AdminPlatform._instance = object.__new__(cls)
                    AdminPlatform.Task_wait_list = []
        return AdminPlatform._instance

    def commit_new_task(self, task):
        """
        Add task to wait list for audit
        :param task:
        :return:
        """
        task.TaskTable.updata_status('inreview')
        self.Task_wait_list.append(task)
        pass

    def confirm_new_task(self, task):
        """
        task Management -> publish task
        :param task:
        :return:
        """
        pass

    @staticmethod
    def get_admin(account):
        sql = 'SELECT * FROM audit_administrator a WHERE a.account=\'%s\';' % (account)
        return Database.execute(sql, response=True)

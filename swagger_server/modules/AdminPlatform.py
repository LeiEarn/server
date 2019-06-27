# -*- coding: utf-8 -*-
import threading
from ..utils.db import Database
from swagger_server.modules.userManagementSystem import ManagementSystem as UMS
from swagger_server.modules.taskManagementSystem import taskManagementSystem as TMS


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

    @staticmethod
    def audit_user(user_id, identity, audit):
        """
        state_prove : U W F S
        :param user_id:  user id
        :param identity: 'S' or 'C'
        :param audit: True or False
        :return:
        """
        user = UMS.get_user_info(user_id)
        if user.isprove != 'W':
            return 'this use is not in the waiting list'

        if identity not in ['S', 'C']:
            return 'identity is wrong or None'

        user = UMS.get_indentity_info(user_id, identity)

        if user is None:
            return 'cannot fount this user in %s' %identity

        if user['state_prove'] != 'W':
            return 'this user is not in the %s waiting list' % identity


        return UMS.audit_user(user_id, identity, audit)

    @staticmethod
    def audit_task(task_id, audit):
        """
        :param task_id:  task id
        :param audit: True or False
        :return:
        """

        task = TMS.get_task_detail(task_id)['task']
        if task['state'] != 'W':
            return 'this wask is not in the waiting list'


        return TMS.audit_task(task_id, audit)



from ..model.User import BasicUser as User
from ..model import Task
from flask import g, session

from AdminPlatform import AdminPlatform

AdminPlatform = AdminPlatform()
class taskManagementSystem(object):
    def __init__(self):
        pass

    """
    发布者：提交任务 -> 
        管理员：审核
        tMS: 写入db（任务状态：待审核）
    """
    def commit_task(self, publisher_id, task_json):
        """
        :param publisher_id:
        :param task:
        :return:
        """

        # create new task and write it to db
        task = Task.TaskTable.create_Task()

        # admin audit this task
        AdminPlatform.commit_new_task(task)

    """
    任务审核成功-> 进行中
    管理平台：正式发布任务
    -> TaskTable 写入database
    """
    def publish_task(self, task):
        task.TaskTable.create_Task(task)
    """
    发布者：增加任务说明
    """
    def add_info(self):
        pass

    """
    发布者：获取发布的任务
    """
    def get_published_tasks(self):
        Task.TaskTable.query_task()
        pass

    """
    获取任务信息
    """
    def get_task_detail(self):
        pass

    """
    获取任务列表
    """
    def get_task_list(self):
        pass

    """
    用户：接受任务
    """
    def accept_task(self):
        pass

    """
    用户：放弃任务
    """
    def abondon_task(self):
        pass

    """
    接受者：提交任务
    """
    def finish_task(self):
        pass

    """
    接受者：提交任务执行情况
    """
    def finish_status(self):
        pass
from ..model.User import User as User
from ..model import Task
from flask import g, session

from AdminPlatform import AdminPlatform

AdminPlatform = AdminPlatform()
class taskManagementSystem(object):
    def __init__(self):
        pass

    
    def commit_task(self, publisher_id, task):
        """发布者：提交任务 -> 管理员：审核
                任务状态：待审核
        :param publisher_id:
        :param task:
        :return:
        """
        AdminPlatform.commit_new_task(task)

    
    def publish_task(self, task):
        """任务审核成功-> 进行中
            管理平台：正式发布任务
            -> TaskTable 写入database
        """
        task.TaskTable.create_Task(task)


    
    def add_info(self):
        """
        发布者：增加任务说明
        """
        pass

    
    def get_published_tasks(self):
        """
        发布者：获取发布的任务
        """
        Task.TaskTable.query_task()
        pass

    
    def abort_task(self):
        """
        发布者：终止任务
        """
        pass

    
    def get_task_detail(self):
        """
        获取任务信息
        """
        pass

    
    def get_task_list(self):
        """
        获取任务列表
        """
        pass

    
    def accept_task(self):
        """
        用户：接受任务
        """
        pass

    
    def abondon_task(self):
        """
        用户：放弃任务
        """
        pass

    
    def commit_job(self):
        """
        接受者：提交任务
        """
        pass

    
    def commit_status(self):
        """
        接受者：提交任务执行情况
        """
        pass
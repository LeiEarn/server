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


    def publish_task(self, task):
        """任务审核成功-> 进行中
            管理平台：正式发布任务
            -> TaskTable 写入database
        """
        task.taskTable.create_task(task)



    def add_info(self):
        """
        发布者：增加任务说明
        """
        pass


    def get_published_tasks(self, user_id):
        """
        发布者：获取发布的任务
        """
        if user_id is not g.user_id:
            return None
        else:
            task = Task.taskTable.get_published_task(user_id)
        return task
        pass


    def abort_task(self, user_id):
        """
        发布者：终止任务
        """
        if user_id is not g.user_id:
            return None
        else:
            task = Task.taskTable.get_published_task(user_id)
        pass


    def get_task_detail(self, task_id):
        """
        获取任务信息
        """

        task = Task.taskTable.get_task_info(task_id)
        return task
        pass


    def get_task_list(self, page_id):
        """
        获取任务列表
        """
        tasks = Task.taskTable.get_task(page_id, 10)
        pass

    def get_accepted_tasks(self, user_id):

        tasks = Task.taskTable.get_accepted_task(union_id = g.union_id)

    def accept_task(self, user_id,  task_id):
        """
        用户：接受任务
        """
        if user_id is not g.user_id:
            return None

        result = Task.taskTable.accept_task(user_id, task_id)
        pass


    def abondon_task(self, user_id, task_id):
        """
        用户：放弃任务
        """
        if user_id is not g.user_id:
            return None

        result = Task.taskTable.abondon_task(user_id, task_id)
        pass


    def commit_job(self, user_id, task_id):
        """
        接受者：提交任务
        """
        result = Task.taskTable.commit_job(user_id, task_id)
        pass


    def commit_status(self):
        """
        接受者：提交任务执行情况
        """
        pass
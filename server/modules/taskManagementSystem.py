from ..model.User import User as User
from flask import g, session
class taskManagementSystem(object):
    def __init__(self):
        pass

    """
    发布者：发布任务
    """
    def publish_task(self):
        pass

    """
    发布者：增加任务说明
    """
    def add_info(self):
        pass

    """
    发布者：获取发布的任务
    """
    def get_published_tasks(self):
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
    接受者：接受任务
    """
    def accept_task(self):
        pass

    """
    接受者：放弃任务
    """
    def abondon_task(self):
        pass

    """
    接受者：提交任务
    """
    def commit_task(self):
        pass

    """
    接受者：提交任务执行情况
    """
    def commit_status(self):
        pass
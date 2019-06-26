# -*- coding: utf-8 -*-
from ..models.model.Task import Task
from ..models.model.User import User as User

from flask import g, session

from .AdminPlatform import AdminPlatform

AdminPlatform = AdminPlatform()
class taskManagementSystem(object):
    def __init__(self):
        pass

    """
    发布者：提交任务 -> 
        管理员：审核
        tMS: 写入db（任务状态：待审`核）
    """
    def commit_task(self,
            publish_id,
            title,
            task_type,
            wjx_id,
            task_intro,
            max_num,
            participants_num,
            money,
            sign_start_time,
            sign_end_time):
        """
        :param publisher_id:
        :param task:
        :return:
        """

        # create new task and write it to db
        task = Task.taskTable.create_task(
            publish_id = g.get('persistent').get('user_id'),
            title = title,
            type_ =task_type,
            wjx_id=wjx_id,
            task_intro=task_intro,
            max_num=max_num,
            participants_num=participants_num,
            money=money,
            sign_start_time=sign_start_time,
            sign_end_time=sign_end_time)

        # admin audit this task
        AdminPlatform.commit_new_task(task)


    def publish_task(self, task):
        """任务审核成功-> 进行中
            管理平台：正式发布任务
            -> TaskTable 写入database
        """
        #task.taskTable.create_task(task)



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
        tasks = Task.taskTable.get_tasks(page_id, 10)
        return tasks

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

    """
        获取信息模块
    """
    @staticmethod
    def get_task_count(user_type='all'):
        return Task.taskTable.task_count(user_type)

    @staticmethod
    def get_tasks(task_type='all', page=0):
        return Task.taskTable.get_tasks(task_type=task_type,
                                        begin=page*100,
                                        end=(page+1)*100)


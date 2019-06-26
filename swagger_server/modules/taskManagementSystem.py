# -*- coding: utf-8 -*-
from ..models.model.Task import Task
from ..models.model.User import User as User
import datetime
from flask import g, session

from .AdminPlatform import AdminPlatform

AdminPlatform = AdminPlatform()
class taskManagementSystem(object):
    def __init__(self):
        pass

    """
    
    """
    def commit_task(self, task):
        """
        发布者：提交任务 -> 
        管理员：审核
        tMS: 写入db（任务状态：待审`核）

        :param publisher_id:
        :param task:
        :return:
        """
        start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # create new task and write it to db
        result = Task.taskTable.create_task(
            publish_id = g.get('persistent').get('user_id'),
            title = task.title,
            type_ =task.task_type,
            wjx_id=task.wjx_id,
            task_intro=task.task_intro,
            max_num=task.max_num,
            participants_num=task.participants_num,
            money=task.money,
            sign_start_time=start_time,
            sign_end_time=task.sign_end_time)
        if  isinstance(result, Exception):
            return ('error', "create fail")
        # admin audit this task
        AdminPlatform.commit_new_task(task)

    

    def publish_task(self, task):
        """任务审核成功-> 进行中
            管理平台：正式发布任务
            -> TaskTable 写入database
        """
        #task.taskTable.create_task(task)


    def add_info(self, task_id, content):
        """
        发布者：增加任务说明
        """
        result = Task.taskTable.append_task_intro(task_id, content)
        if not  isinstance(result, Exception):
            return result
        else:
            return ('error', "fail")


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


    def abort_task(self, task_id, user_id):
        """
        发布者：终止任务
        """
        if user_id is not g.user_id:
            return ('error', 'user identity error')
        else:
            task = Task.taskTable.get_task_info(task_id=task_id)
            
            if task is not None and 'participants_num' in task:
                number = task['participants_num']
                if number ==0:
                    result = Task.taskTable.abort_task(task['task_id'])
                    if not isinstance(result, Exception):
                        return ('success')
                    else:
                        return ('error', 'unknown error')
                else:
                    return ('error', 'participants is not zero')
            else:
                return ('error', 'task not exist')

    def get_task_accepter(self, task_id, user_id):
        if user_id ==  g.get('persistent').get('user_id'):
            return ('error', 'identity error')
        task = Task.taskTable.get_task_info(task_id = task_id)
        if task is None:
            return ('error', 'no such task')
        accepters = Task.taskTable.get_task_participants(task_id = task_id)
        return accepters


    def get_task_detail(self, task_id):
        """
        获取任务信息以及发布者信息
        """

        task = Task.taskTable.get_task_info(task_id)
        if task is None:
            return ('error', 'no such task')
        user = User.table.get_user_info(user_id=task['publish_id'])

        return task, user

    def get_related_tasks(self, userId, Type):
        if Type =="acceptment":
            result = Task.taskTable.get_accepted_task(user_id=userId)
        elif Type == "publishment":
            result = Task.taskTable.get_accepted_task(user_id = userId)
        return result



    def get_task_list(self, page_id):
        """
        获取任务列表
        """
        tasks = Task.taskTable.get_tasks(page_id, 10)
        return tasks

    def get_accepted_tasks(self, user_id):
        if user_id is not g.user_id:
            return None
        tasks = Task.taskTable.get_accepted_task(user_id = g.user_id)

    def get_task_jobs(self, task_id):
        result = Task.taskTable.get_task_jobs(task_id)
        return result
    def accept_task(self, user_id,  task_id):
        """
        用户：接受任务
        """
        if user_id is not g.user_id:
            return None

        result = Task.taskTable.participate_task(user_id, task_id)
        return result


    def abondon_task(self, user_id, task_id):
        """
        用户：放弃任务
        """
        if user_id is not g.user_id:
            return None

        result = Task.taskTable.abondon_task(user_id, task_id)
        return result
        pass


    def commit_job(self, user_id, task_id, job):
        """
        接受者：提交任务
        """
        files = job.files
        result = Task.taskTable.commit_job(user_id=user_id, task_id,=task_id files=files )
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
    def get_task_count(state='all', type='O'):
        return Task.taskTable.task_count(state, type)

    @staticmethod
    def get_tasks(task_type='all', page=0):
        return Task.taskTable.get_tasks(task_type=task_type,
                                        begin=page*100,
                                        end=(page+1)*100)


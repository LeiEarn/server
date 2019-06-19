# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user_login import UserLogin
from .api.user_prove import UserProve
from .api.user_modify import UserModify
from .api.task_getTask import TaskGettask
from .api.task_getTaskDetail import TaskGettaskdetail


routes = [
    dict(resource=UserLogin, urls=['/user/login'], endpoint='user_login'),
    dict(resource=UserProve, urls=['/user/prove'], endpoint='user_prove'),
    dict(resource=UserModify, urls=['/user/modify'], endpoint='user_modify'),
    dict(resource=TaskGettask, urls=['/task/getTask'], endpoint='task_getTask'),
    dict(resource=TaskGettaskdetail, urls=['/task/getTaskDetail'], endpoint='task_getTaskDetail'),
]
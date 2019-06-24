# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.login import Login
from .api.prove import Prove
from .api.modify import Modify
from .api.getProveState import Getprovestate
from .api.getBalance import Getbalance
from .api.reCharge import Recharge
from .api.createGroup import Creategroup
from .api.joinGroup import Joingroup
from .api.getGroup import Getgroup
from .api.getCreatedGroup import Getcreatedgroup
from .api.getJoinedGroup import Getjoinedgroup
from .api.getTask import Gettask
from .api.getPublishedTask import Getpublishedtask
from .api.getAcceptedTask import Getacceptedtask
from .api.getTaskDetail import Gettaskdetail
from .api.acceptTask import Accepttask
from .api.commitJob import Commitjob
from .api.addTaskInfo import Addtaskinfo
from .api.abandonTask import Abandontask
from .api.abortTask import Aborttask
from .api.publishTask import Publishtask


routes = [
    dict(resource=Login, urls=['/login'], endpoint='login'),
    dict(resource=Prove, urls=['/prove'], endpoint='prove'),
    dict(resource=Modify, urls=['/modify'], endpoint='modify'),
    dict(resource=Getprovestate, urls=['/getProveState'], endpoint='getProveState'),
    dict(resource=Getbalance, urls=['/getBalance'], endpoint='getBalance'),
    dict(resource=Recharge, urls=['/reCharge'], endpoint='reCharge'),
    dict(resource=Creategroup, urls=['/createGroup'], endpoint='createGroup'),
    dict(resource=Joingroup, urls=['/joinGroup'], endpoint='joinGroup'),
    dict(resource=Getgroup, urls=['/getGroup'], endpoint='getGroup'),
    dict(resource=Getcreatedgroup, urls=['/getCreatedGroup'], endpoint='getCreatedGroup'),
    dict(resource=Getjoinedgroup, urls=['/getJoinedGroup'], endpoint='getJoinedGroup'),
    dict(resource=Gettask, urls=['/getTask'], endpoint='getTask'),
    dict(resource=Getpublishedtask, urls=['/getPublishedTask'], endpoint='getPublishedTask'),
    dict(resource=Getacceptedtask, urls=['/getAcceptedTask'], endpoint='getAcceptedTask'),
    dict(resource=Gettaskdetail, urls=['/getTaskDetail'], endpoint='getTaskDetail'),
    dict(resource=Accepttask, urls=['/acceptTask'], endpoint='acceptTask'),
    dict(resource=Commitjob, urls=['/commitJob'], endpoint='commitJob'),
    dict(resource=Addtaskinfo, urls=['/addTaskInfo'], endpoint='addTaskInfo'),
    dict(resource=Abandontask, urls=['/abandonTask'], endpoint='abandonTask'),
    dict(resource=Aborttask, urls=['/abortTask'], endpoint='abortTask'),
    dict(resource=Publishtask, urls=['/publishTask'], endpoint='publishTask'),
]
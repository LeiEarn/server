import connexion
import six

from swagger_server.models.cert import Cert  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.extra_task_info import ExtraTaskInfo  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.task_detail import TaskDetail  # noqa: E501
from swagger_server.models.task_detail_with_publisher import TaskDetailWithPublisher  # noqa: E501
from swagger_server.models.user_info_with_tel import UserInfoWithTel  # noqa: E501
from swagger_server import util
from swagger_server.modules.taskManagementSystem import taskManagementSystem
from swagger_server.modules.accessControlSystem import AccessControlSystem as accessControlSystem

task_mangager = taskManagementSystem()
access_control = accessControlSystem()

login_response=(ErrorResponse('login'),400)
error_response = (ErrorResponse('error'), 400)
@access_control.login_required(login_response)
def task_task_id_accepter_delete(taskId, userId):  # noqa: E501
    """Accepter abandon the task.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: the userId of accepter
    :type userId: str

    :rtype: None
    """
    result = task_mangager.abondon_task(user_id=userId, task_id=taskId)
    if 'error' in result:
        return ErrorResponse(result[1]), 400
    else:
        return result[1], 200


@access_control.login_required(login_response)
def task_task_id_accepter_get(taskId, userId):  # noqa: E501
    """Publisher get the info of accepters

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: the userId of publisher
    :type userId: str

    :rtype: List[UserInfoWithTel]
    """
    results = task_mangager.get_task_accepter(task_id=taskId, user_id = userId)
    if len(results) is not 0 and results[0] is 'error':
        return []
    else:
        return [
            UserInfoWithTel(
                avatar_url= results['photo'],
                nick_name=results['nickname'],
                tel=results['phone'],
                user_id=results['user_id']) 
            for item in results
        ]


@access_control.login_required(login_response)
def task_task_id_accepter_post(taskId, userId):  # noqa: E501
    """User accept the task.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: the userId of user ready to accept
    :type userId: str

    :rtype: None
    """
    result = task_mangager.accept_task(user_id=userId, task_id=taskId)
    if 'error' in result:
        return ErrorResponse(result[1]), 400
    else:
        return 'success', 200

    return 'do some magic!'


@access_control.login_required(login_response)
def task_task_id_info_delete(taskId, userId):  # noqa: E501
    """Publisher abort the task.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str

    :rtype: None
    """
    result = task_mangager.abort_task(task_id=taskId, user_id = userId)
    if 'error' in result:
        return ErrorResponse(result[1]), 400
    else:
        return 'success', 200


def task_task_id_info_get(taskId):  # noqa: E501
    """Returns one task&#39;s detail

    Returns one task&#39;s detail # noqa: E501

    :param taskId: The task&#39;s id in database.
    :type taskId: str

    :rtype: TaskDetailWithPublisher
    """
    task_with_publisher = task_mangager.get_task_detail(task_id=taskId)
    if 'error' in task_with_publisher:
        return ErrorResponse(task_with_publisher[1]), 400
    else:
        #?需要做处理
        if "publisher" in task_with_publisher and task_with_publisher['publisher'] is not None :
            user =UserInfoWithTel(
                user_id= task_with_publisher['publisher']['user_id'],
                avatar_url=task_with_publisher['publisher']['photo'],
                tel=task_with_publisher['publisher']['phone_number']
            )
        else:
            user =None
        if "task" in task_with_publisher and task_with_publisher['task'] is not None :
            content=TaskDetail(
                type=task_with_publisher['task']["type"],
                wjx_id=task_with_publisher['task']["wjx_id"],
                title=task_with_publisher['task']["title"],
                time=task_with_publisher['task']["sign_end_time"],
                max_num=task_with_publisher['task']["max_num"],
                money=task_with_publisher['task']["money"]
            )
        else:
            content =None
        return TaskDetailWithPublisher(
            user = user,
            content= content,
            has_received=task_with_publisher.get('task_job_state')
        )
    return 'do some magic!'


@access_control.login_required(login_response)
def task_task_id_info_put(taskId, body):  # noqa: E501
    """Publisher add the task info.

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ExtraTaskInfo.from_dict(connexion.request.get_json())  # noqa: E501
    result= task_mangager.add_info(task_id=taskId, content = body.content)
    if result is  None or 'error' in result:
        return ErrorResponse('add fail'), 400
    else:
        return 'success', 200


def task_task_id_job_get(taskId, userId):  # noqa: E501
    """User get all the Job.

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str

    :rtype: List[Cert]
    """
    result = task_mangager.get_task_jobs(task_id=taskId)
    if len(result) > 0 and 'error' is result[0]:
        return ErrorResponse(result[1]), 400
    else:
        return [
            Cert(
                user_id= item['user_id'],
                files=item['files'],
                remarks=item['remarks']
            )
            for item in result
        ]


@access_control.login_required(login_response)
def task_task_id_job_post(taskId, body):  # noqa: E501
    """User commit the job.

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Cert.from_dict(connexion.request.get_json())  # noqa: E501
    
    result = task_mangager.commit_job(user_id=body.user_id,task_id=taskId,job =body )
    if result is  None or 'error' in result:
        return ErrorResponse('post fail'), 400
    else:
        return 'success', 200


@access_control.login_required(login_response)
def task_task_id_job_put(taskId, userId, state):  # noqa: E501
    """Publisher agree the job of the user.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str
    :param state: agree, reject
    :type state: str

    :rtype: None
    """
    result = task_mangager.agree_job(task_id=taskId, user_id=userId, state=state)
    if 'error' in result:
        return ErrorResponse(result[1]), 400
    else:
        return 'success', 200


@access_control.login_required(login_response)
def task_user_id_get(userId, type):  # noqa: E501
    """Returns all his own published or accepted tasks in the page.

    Returns the published tasks, the max number is 10. If the page is the last page, the return all left. # noqa: E501

    :param userId: 
    :type userId: str
    :param type: acceptment or publishment
    :type type: str

    :rtype: List[Task]
    """
    tasks = task_mangager.get_related_tasks(userId=userId, Type=type)
    if tasks is None:
        return ErrorResponse("error"), 400
    else:
        return [ 
            Task(
                id = item['task_id'],
                money= item['money'],
                icon= item['icon'],
                title=item['title'],
                max_num=item['max_num'],
                desc=item['task_intro'],
                part_num=item['participants_num']
            )
            for item in tasks
         ]   
    return 'do some magic!'


@access_control.login_required(login_response)
def task_user_id_post(userId, body):  # noqa: E501
    """User publish the task.

     # noqa: E501

    :param userId: 
    :type userId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TaskDetail.from_dict(connexion.request.get_json())  # noqa: E501
    result = task_mangager.commit_task(body)
    if 'error' in result:
        return ErrorResponse(result[1]), 400
    else:
        return 'success', 200


@access_control.login_required(login_response)
def tasks_get(pageId, type=None):  # noqa: E501
    """Returns all related tasks according to the pageId.

    Returns the published tasks, the max number is 10. If the page is the last page, the return all left. # noqa: E501

    :param pageId: Page number
    :type pageId: int
    :param type: default, recommend, easy
    :type type: str

    :rtype: List[Task]
    """
    tasks = task_mangager.get_task_list(page_id = pageId)
    if tasks is None:
        return ErrorResponse("error"), 400
    else:
        return [ 
            Task(
                id = item['task_id'],
                money= item['money'],
                icon= item['icon'],
                title=item['title'],
                max_num=item['max_num'],
                desc=item['task_intro'],
                part_num=item['participants_num']
            )
            for item in tasks
         ]
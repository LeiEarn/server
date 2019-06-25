import connexion
import six

from swagger_server.models.cert import Cert  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.extra_task_info import ExtraTaskInfo  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.task_detail_with_publisher import TaskDetailWithPublisher  # noqa: E501
from swagger_server.models.task_detail_with_user_id import TaskDetailWithUserId  # noqa: E501
from swagger_server.models.user_info_with_tel import UserInfoWithTel  # noqa: E501
from swagger_server import util
from swagger_server.modules.taskManagementSystem import taskManagementSystem
from swagger_server.modules.accessControlSystem import AccessControlSystem as accessControlSystem

task_mangager = taskManagementSystem()
access_control = accessControlSystem()

def task_task_id_accepter_delete(taskId, userId):  # noqa: E501
    """Accepter abandon the task.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str

    :rtype: None
    """
    return 'do some magic!'


def task_task_id_accepter_post(taskId, body):  # noqa: E501
    """User commit the job.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Cert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def task_task_id_get(taskId):  # noqa: E501
    """Returns one task&#39;s detail

    Returns one task&#39;s detail # noqa: E501

    :param taskId: The task&#39;s id in database.
    :type taskId: str

    :rtype: TaskDetailWithPublisher
    """
    return 'do some magic!'


def task_task_id_publisher_delete(taskId, userId):  # noqa: E501
    """Publisher abort the task.

    This operation shows how to override the global security defined above, as we want to open it up for all users. # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str

    :rtype: None
    """
    return 'do some magic!'


def task_task_id_publisher_get(taskId, userId):  # noqa: E501
    """Publisher get the info of accepters

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param userId: 
    :type userId: str

    :rtype: List[UserInfoWithTel]
    """
    return 'do some magic!'


def task_task_id_publisher_post(taskId, body):  # noqa: E501
    """User publish the task.

     # noqa: E501

    :param taskId: 
    :type taskId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TaskDetailWithUserId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def task_task_id_publisher_put(taskId, body):  # noqa: E501
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
    return 'do some magic!'


def task_user_id_acceptment_get(userId):  # noqa: E501
    """Returns all his accepted tasks in the page.

    Returns the published tasks, the max number is 10. If the page is the last page, the return all left. # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: List[Task]
    """
    return 'do some magic!'


def task_user_id_publishment_get(userId):  # noqa: E501
    """Returns all his own published tasks in the page.

    Returns the published tasks, the max number is 10. If the page is the last page, the return all left. # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: List[Task]
    """
    return 'do some magic!'


def tasks_get(pageId):  # noqa: E501
    """Returns all related tasks according to the pageId.

    Returns the published tasks, the max number is 10. If the page is the last page, the return all left. # noqa: E501

    :param pageId: Page number
    :type pageId: int

    :rtype: List[Task]
    """
    tasks = task_mangager.get_task_list(page_id = pageId)
    if tasks is None:
        return ErrorResponse("error")
    else:
        return ""
    return 'do some magic!'

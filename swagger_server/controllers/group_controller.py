import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.groups import Groups  # noqa: E501
from swagger_server.models.my_group import MyGroup  # noqa: E501
from swagger_server import util


def group_user_id_delete(userId, groupName):  # noqa: E501
    """User quits the task.

     # noqa: E501

    :param userId: 
    :type userId: str
    :param groupName: 
    :type groupName: str

    :rtype: None
    """
    return 'do some magic!'


def group_user_id_get(userId):  # noqa: E501
    """User get his join or created group.

     # noqa: E501

    :param userId: 
    :type userId: str

    :rtype: MyGroup
    """
    return 'do some magic!'


def group_user_id_post(userId, groupName):  # noqa: E501
    """User creates the group.

     # noqa: E501

    :param userId: 
    :type userId: str
    :param groupName: 
    :type groupName: str

    :rtype: None
    """
    return 'do some magic!'


def group_user_id_put(userId, groupName):  # noqa: E501
    """User joins the task.

     # noqa: E501

    :param userId: 
    :type userId: str
    :param groupName: 
    :type groupName: str

    :rtype: None
    """
    return 'do some magic!'


def groups_get():  # noqa: E501
    """User get the all group.

     # noqa: E501


    :rtype: Groups
    """
    return 'do some magic!'

import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.url import Url  # noqa: E501
from swagger_server import util


def image_post(image):  # noqa: E501
    """upload image

     # noqa: E501

    :param image: image
    :type image: werkzeug.datastructures.FileStorage

    :rtype: Url
    """
    return 'do some magic!'

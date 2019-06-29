# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.groups import Groups  # noqa: F401,E501
from swagger_server import util


class MyGroup(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, created: Groups = None, joined: Groups = None):  # noqa: E501
        """MyGroup - a model defined in Swagger

        :param created: The created of this MyGroup.  # noqa: E501
        :type created: Groups
        :param joined: The joined of this MyGroup.  # noqa: E501
        :type joined: Groups
        """
        self.swagger_types = {"created": Groups, "joined": Groups}

        self.attribute_map = {"created": "created", "joined": "joined"}

        self._created = created
        self._joined = joined

    @classmethod
    def from_dict(cls, dikt) -> "MyGroup":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MyGroup of this MyGroup.  # noqa: E501
        :rtype: MyGroup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self) -> Groups:
        """Gets the created of this MyGroup.


        :return: The created of this MyGroup.
        :rtype: Groups
        """
        return self._created

    @created.setter
    def created(self, created: Groups):
        """Sets the created of this MyGroup.


        :param created: The created of this MyGroup.
        :type created: Groups
        """

        self._created = created

    @property
    def joined(self) -> Groups:
        """Gets the joined of this MyGroup.


        :return: The joined of this MyGroup.
        :rtype: Groups
        """
        return self._joined

    @joined.setter
    def joined(self, joined: Groups):
        """Sets the joined of this MyGroup.


        :param joined: The joined of this MyGroup.
        :type joined: Groups
        """

        self._joined = joined

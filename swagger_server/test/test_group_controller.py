# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.groups import Groups  # noqa: E501
from swagger_server.models.my_group import MyGroup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGroupController(BaseTestCase):
    """GroupController integration test stubs"""

    def test_group_user_id_delete(self):
        """Test case for group_user_id_delete

        User quits the task.
        """
        query_string = [("groupName", "groupName_example")]
        response = self.client.open(
            "//group/{userId}".format(userId="userId_example"),
            method="DELETE",
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_group_user_id_get(self):
        """Test case for group_user_id_get

        User get his join or created group.
        """
        response = self.client.open(
            "//group/{userId}".format(userId="userId_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_group_user_id_post(self):
        """Test case for group_user_id_post

        User creates the group.
        """
        query_string = [("groupName", "groupName_example")]
        response = self.client.open(
            "//group/{userId}".format(userId="userId_example"),
            method="POST",
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_group_user_id_put(self):
        """Test case for group_user_id_put

        User joins the task.
        """
        query_string = [("groupName", "groupName_example")]
        response = self.client.open(
            "//group/{userId}".format(userId="userId_example"),
            method="PUT",
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_groups_get(self):
        """Test case for groups_get

        User get the all group.
        """
        response = self.client.open("//groups", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.iden_info import IdenInfo  # noqa: E501
from swagger_server.models.iden_info_with_credit import IdenInfoWithCredit  # noqa: E501
from swagger_server.models.login_code import LoginCode  # noqa: E501
from swagger_server.models.prove_state import ProveState  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.models.user_info_without_id import UserInfoWithoutId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_info_put(self):
        """Test case for user_info_put

        User modify his basic info.
        """
        body = UserInfoWithoutId()
        response = self.client.open(
            "//user/info",
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_proof_get(self):
        """Test case for user_proof_get

        get user's indentity info
        """
        query_string = [("userId", "userId_example")]
        response = self.client.open(
            "//user/proof", method="GET", query_string=query_string
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_proof_post(self):
        """Test case for user_proof_post

        User provide his prove identity.
        """
        body = IdenInfo()
        response = self.client.open(
            "//user/proof",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_session_post(self):
        """Test case for user_session_post

        Users login
        """
        body = LoginCode()
        response = self.client.open(
            "//user/session",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_user_id_balance_get(self):
        """Test case for user_user_id_balance_get

        User get the balance.
        """
        response = self.client.open(
            "//user/{userId}/balance".format(userId="userId_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_user_id_balance_put(self):
        """Test case for user_user_id_balance_put

        User recharge.
        """
        query_string = [("money", "money_example")]
        response = self.client.open(
            "//user/{userId}/balance".format(userId="userId_example"),
            method="PUT",
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_user_user_id_proof_state_get(self):
        """Test case for user_user_id_proof_state_get

        User get his proveState.
        """
        response = self.client.open(
            "//user/{userId}/proof/state".format(userId="userId_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()

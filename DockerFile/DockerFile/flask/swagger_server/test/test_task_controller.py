# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cert import Cert  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.extra_task_info import ExtraTaskInfo  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.task_detail import TaskDetail  # noqa: E501
from swagger_server.models.task_detail_with_publisher import TaskDetailWithPublisher  # noqa: E501
from swagger_server.models.user_info_with_tel import UserInfoWithTel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTaskController(BaseTestCase):
    """TaskController integration test stubs"""

    def test_task_task_id_accepter_delete(self):
        """Test case for task_task_id_accepter_delete

        Accepter abandon the task.
        """
        query_string = [('userId', 'userId_example')]
        response = self.client.open(
            '//task/{taskId}/accepter'.format(taskId='taskId_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_accepter_get(self):
        """Test case for task_task_id_accepter_get

        Publisher get the info of accepters
        """
        query_string = [('userId', 'userId_example')]
        response = self.client.open(
            '//task/{taskId}/accepter'.format(taskId='taskId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_accepter_post(self):
        """Test case for task_task_id_accepter_post

        User accept the task.
        """
        query_string = [('userId', 'userId_example')]
        response = self.client.open(
            '//task/{taskId}/accepter'.format(taskId='taskId_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_info_delete(self):
        """Test case for task_task_id_info_delete

        Publisher abort the task.
        """
        query_string = [('userId', 'userId_example')]
        response = self.client.open(
            '//task/{taskId}/info'.format(taskId='taskId_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_info_get(self):
        """Test case for task_task_id_info_get

        Returns one task's detail
        """
        response = self.client.open(
            '//task/{taskId}/info'.format(taskId='taskId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_info_put(self):
        """Test case for task_task_id_info_put

        Publisher add the task info.
        """
        body = ExtraTaskInfo()
        response = self.client.open(
            '//task/{taskId}/info'.format(taskId='taskId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_job_get(self):
        """Test case for task_task_id_job_get

        User get all the Job.
        """
        query_string = [('userId', 'userId_example')]
        response = self.client.open(
            '//task/{taskId}/job'.format(taskId='taskId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_job_post(self):
        """Test case for task_task_id_job_post

        User commit the job.
        """
        body = Cert()
        response = self.client.open(
            '//task/{taskId}/job'.format(taskId='taskId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_task_id_job_put(self):
        """Test case for task_task_id_job_put

        Publisher agree the job of the user.
        """
        query_string = [('userId', 'userId_example'),
                        ('state', 'state_example')]
        response = self.client.open(
            '//task/{taskId}/job'.format(taskId='taskId_example'),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_user_id_get(self):
        """Test case for task_user_id_get

        Returns all his own published or accepted tasks in the page.
        """
        query_string = [('type', 'type_example')]
        response = self.client.open(
            '//task/{userId}'.format(userId='userId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_user_id_post(self):
        """Test case for task_user_id_post

        User publish the task.
        """
        body = TaskDetail()
        response = self.client.open(
            '//task/{userId}'.format(userId='userId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tasks_get(self):
        """Test case for tasks_get

        Returns all related tasks according to the pageId.
        """
        query_string = [('pageId', 0),
                        ('type', 'default')]
        response = self.client.open(
            '//tasks',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
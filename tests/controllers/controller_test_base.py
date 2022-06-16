# -*- coding: utf-8 -*-

"""
managementservice

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import unittest
from tests.http_response_catcher import HttpResponseCatcher
from managementservice.configuration import Configuration
from managementservice.configuration import Environment
from managementservice.managementservice_client import ManagementserviceClient

class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ControllerTestBase.create_configuration()
        cls.client = ManagementserviceClient(config=cls.config)

    @staticmethod
    def create_configuration():
        return Configuration(http_call_back=HttpResponseCatcher())

import http.client
import sys
import unittest
from unittest.mock import patch

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import http


class TestHttpclientMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = sys.modules[__name__]
        cls.recorder, _ = setup_recording(cls.module, {sys, unittest, sr})

        cls.host = 'www.example.com'
        cls.connectionHTTP = http.client.HTTPConnection(cls.host)
        cls.connectionHTTPS = http.client.HTTPSConnection(cls.host)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    @patch('http.client.HTTPConnection.connect')
    def test_connectHTTP(self, mock_connect):
        with recording_activated():
            self.connectionHTTP.connect()
        self.assertTrue(
            is_recorded(
                self.recorder, http.client, http.client.HTTPConnection, 'connect'
            )
        )

    @patch('http.client.HTTPSConnection.connect')
    def test_connectHTTPS(self, mock_connect):
        with recording_activated():
            self.connectionHTTPS.connect()
        self.assertTrue(
            is_recorded(
                self.recorder, http.client, http.client.HTTPSConnection, 'connect'
            )
        )

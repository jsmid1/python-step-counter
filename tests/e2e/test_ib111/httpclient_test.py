import http.client
import sys
import unittest
from unittest.mock import patch

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import http


class TestHttpclientMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

        self.host = 'www.example.com'
        self.connectionHTTP = http.client.HTTPConnection(self.host)
        self.connectionHTTPS = http.client.HTTPSConnection(self.host)

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    @patch('http.client.HTTPConnection.connect')
    def test_connectHTTP(self, mock_connect):
        self.connectionHTTP.connect()
        with RecodingActivated():
            self.connectionHTTP.close()
        self.assertTrue(
            is_recorded(self.recorder, http.client, http.client.HTTPConnection, 'close')
        )

    @patch('http.client.HTTPSConnection.connect')
    def test_connectHTTPS(self, mock_connect):
        self.connectionHTTPS.connect()
        with RecodingActivated():
            self.connectionHTTPS.close()
        self.assertTrue(
            is_recorded(
                self.recorder, http.client, http.client.HTTPSConnection, 'close'
            )
        )

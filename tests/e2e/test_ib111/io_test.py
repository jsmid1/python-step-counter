import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import io


class TestIoMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_io_BytesIO_getbuffer(self):
        bytesio = io.BytesIO(b'test data')
        with RecodingActivated():
            bytesio.getbuffer()
        self.assertTrue(is_recorded(self.recorder, io, io.BytesIO, 'getbuffer'))

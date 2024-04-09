import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import zipfile


class TestZipfileMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = sys.modules[__name__]
        cls.recorder, _ = setup_recording(cls.module, {sys, unittest, sr})

        os.chdir('tests/test_files/')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_zipfile_Zipfile_close(self):
        zip_file = zipfile.ZipFile('test_zip.zip')
        with recording_activated():
            zip_file.close()
        self.assertTrue(is_recorded(self.recorder, zipfile, zipfile.ZipFile, 'close'))

    def test_zipfile_is_zipfile(self):
        with recording_activated():
            zipfile.is_zipfile('test.zip')
        self.assertTrue(is_recorded(self.recorder, zipfile, None, 'is_zipfile'))

import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import csv


class TestTurtleMethods(unittest.TestCase):
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

    def test_csv_reader(self):
        with recording_activated():
            with open('file.csv', newline='') as csvfile:
                csv.reader(csvfile)
        self.assertTrue(is_recorded(self.recorder, csv, 'reader'))

    def test_csv_writer(self):
        try:
            with open('file.csv', newline=''):
                pass
        except:
            pass

        with recording_activated():
            with open('file.csv', 'w', newline='') as csvfile:
                csv.writer(csvfile)
        self.assertTrue(is_recorded(self.recorder, csv, 'writer'))

    # skip csv.DictReader, no methods are being recorder

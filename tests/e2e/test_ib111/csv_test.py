import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import csv


class TestTurtleMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

        os.chdir('tests/test_files/')

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_csv_reader(self):
        with RecodingActivated():
            with open('file.csv', newline='') as csvfile:
                csv.reader(csvfile)
        self.assertTrue(is_recorded(self.recorder, csv, None, 'reader'))

    def test_csv_writer(self):
        try:
            with open('file.csv', newline=''):
                pass
        except:
            pass

        with RecodingActivated():
            with open('file.csv', 'w', newline='') as csvfile:
                csv.writer(csvfile)
        self.assertTrue(is_recorded(self.recorder, csv, None, 'writer'))

    # skip csv.DictReader, no methods are being recorder

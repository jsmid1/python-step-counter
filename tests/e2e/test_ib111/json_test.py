import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import json


class TestJsonMethods(unittest.TestCase):
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

    def test_json_load(self):
        with RecodingActivated():
            with open('file.json', 'r') as f:
                data = json.load(f)
        self.assertTrue(is_recorded(self.recorder, json, None, 'load'))

    def test_json_loads(self):
        with RecodingActivated():
            data = json.loads('{'key': 'value'}')
        self.assertTrue(is_recorded(self.recorder, json, None, 'loads'))

    def test_json_dump(self):
        with RecodingActivated():
            with open('file.json', 'w') as f:
                json.dump({'key': 'value'}, f)
        self.assertTrue(is_recorded(self.recorder, json, None, 'dump'))

    def test_json_dumps(self):
        with RecodingActivated():
            jsonString = json.dumps({'key': 'value'})
        self.assertTrue(is_recorded(self.recorder, json, None, 'dumps'))

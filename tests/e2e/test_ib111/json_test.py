import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import json


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

    def test_json_load(self):
        with recording_activated():
            with open('file.json', 'r') as f:
                data = json.load(f)
        self.assertTrue(is_recorded(self.recorder, json, 'load'))

    def test_json_loads(self):
        with recording_activated():
            data = json.loads('{"key": "value"}')
        self.assertTrue(is_recorded(self.recorder, json, 'loads'))

    def test_json_dump(self):
        with recording_activated():
            with open('file.json', 'w') as f:
                json.dump({'key': 'value'}, f)
        self.assertTrue(is_recorded(self.recorder, json, 'dump'))

    def test_json_dumps(self):
        with recording_activated():
            jsonString = json.dumps({'key': 'value'})
        self.assertTrue(is_recorded(self.recorder, json, 'dumps'))

import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

dict_values = type({}.values())


class TestDictvaluesMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_dict_values_eq(self):
        with recording_activated():
            x = {'a': 1, 'b': 2}.values() == {'a': 1, 'b': 2}.values()
        self.assertTrue(is_recorded(self.recorder, dict_values, '__eq__'))

    def test_dict_values_ne(self):
        with recording_activated():
            x = {'a': 1, 'b': 2}.values() != {'a': 2, 'b': 3}.values()
        self.assertTrue(is_recorded(self.recorder, dict_values, '__ne__'))

    def test_dict_values_iter(self):
        with recording_activated():
            iter({'a': 1, 'b': 2}.values())
        self.assertTrue(is_recorded(self.recorder, dict_values, '__iter__'))

    def test_dict_values_len(self):
        with recording_activated():
            len({'a': 1, 'b': 2}.values())
        self.assertTrue(is_recorded(self.recorder, dict_values, '__len__'))

    def test_dict_values_repr(self):
        with recording_activated():
            repr({'a': 1, 'b': 2}.values())
        self.assertTrue(is_recorded(self.recorder, dict_values, '__repr__'))

    @unittest.skip('Maps to different function (uses dict_values.__iter__)')
    def test_dict_values_contains(self):
        with recording_activated():
            x = {'a': 1, 'b': 2}.values()
            1 in x
        print(self.recorder.get_data())
        self.assertTrue(is_recorded(self.recorder, dict_values, '__contains__'))

    def test_dict_values_reversed(self):
        with recording_activated():
            x = {'a': 1, 'b': 2}.values()
            reversed(x)

        self.assertTrue(is_recorded(self.recorder, dict_values, '__reversed__'))

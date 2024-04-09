import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import math
import builtins

class TestDictMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_dict_contains(self):
        with recording_activated():
            x = {'key': 'value'}
            'key' in x
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__contains__'))

    @unittest.skip('Setitem internally, banned in restrict')
    def test_dict_delitem(self):
        with recording_activated():
            x = {'key': 'value'}
            del x['key']
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__delitem__'))

    def test_dict_eq(self):
        with recording_activated():
            x = {'key': 'value'}
            x == {'key': 'value'}
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__eq__'))

    def test_dict_getitem(self):
        with recording_activated():
            x = {'key': 'value'}
            x['key']
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__getitem__'))

    # TODO change after patching fix
    @unittest.skip('Not being patched')
    def test_dict_iter(self):
        with recording_activated():
            x = {'key': 'value'}
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__iter__'))

    def test_dict_len(self):
        with recording_activated():
            x = {'key': 'value'}
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__len__'))

    def test_dict_ne(self):
        with recording_activated():
            x = {'key': 'value'}
            x != {'another_key': 'value'}
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__ne__'))

    @unittest.skip('Not recorder')
    def test_dict_setitem(self):
        with recording_activated():
            x = {}
            x['key'] = 'value'
        self.assertTrue(is_recorded(self.recorder, builtins, dict, '__setitem__'))

    # Non-dunder methods
    def test_dict_clear(self):
        with recording_activated():
            x = {'key': 'value'}
            x.clear()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'clear'))

    def test_dict_copy(self):
        with recording_activated():
            x = {'key': 'value'}
            x.copy()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'copy'))

    def test_dict_fromkeys(self):
        with recording_activated():
            dict.fromkeys(['key'], 'value')
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'fromkeys'))

    def test_dict_get(self):
        with recording_activated():
            x = {'key': 'value'}
            x.get('key')
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'get'))

    def test_dict_items(self):
        with recording_activated():
            x = {'key': 'value'}
            x.items()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'items'))

    def test_dict_keys(self):
        with recording_activated():
            x = {'key': 'value'}
            x.keys()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'keys'))

    def test_dict_pop(self):
        with recording_activated():
            x = {'key': 'value'}
            x.pop('key')
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'pop'))

    def test_dict_popitem(self):
        with recording_activated():
            x = {'key': 'value'}
            x.popitem()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'popitem'))

    def test_dict_setdefault(self):
        with recording_activated():
            x = {'key': 'value'}
            x.setdefault('key', 'default')
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'setdefault'))

    def test_dict_update(self):
        with recording_activated():
            x = {'key': 'value'}
            x.update({'another_key': 'another_value'})
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'update'))

    def test_dict_values(self):
        with recording_activated():
            x = {'key': 'value'}
            x.values()
        self.assertTrue(is_recorded(self.recorder, builtins, dict, 'values'))

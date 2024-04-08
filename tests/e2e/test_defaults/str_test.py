import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import math


class TestStrMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    @unittest.skip('str.__add__ is not used, new string is created instead')
    def test_str_add(self):
        with recording_activated():
            x = "Hello"
            x + " World"
        self.assertTrue(is_recorded(self.recorder, str, '__add__'))

    def test_str_contains(self):
        with recording_activated():
            x = "Hello"
            "H" in x
        self.assertTrue(is_recorded(self.recorder, str, '__contains__'))

    def test_str_eq(self):
        with recording_activated():
            x = "Hello"
            x == "Hello"
        self.assertTrue(is_recorded(self.recorder, str, '__eq__'))

    def test_str_getitem(self):
        with recording_activated():
            x = "Hello"
            x[0]
        self.assertTrue(is_recorded(self.recorder, str, '__getitem__'))

    def test_str_iter(self):
        with recording_activated():
            x = "Hello"
            iter(x)
        self.assertTrue(is_recorded(self.recorder, str, '__iter__'))

    def test_str_len(self):
        with recording_activated():
            x = "Hello"
            len(x)
        self.assertTrue(is_recorded(self.recorder, str, '__len__'))

    @unittest.skip('Creates a new string')
    def test_str_mod(self):
        with recording_activated():
            x = "%s World"
            x % "Hello"
        self.assertTrue(is_recorded(self.recorder, str, '__mod__'))

    def test_str_mul(self):
        with recording_activated():
            x = "Hello"
            x * 2
        self.assertTrue(is_recorded(self.recorder, str, '__mul__'))

    def test_str_ne(self):
        with recording_activated():
            x = "Hello"
            x != "World"
        self.assertTrue(is_recorded(self.recorder, str, '__ne__'))

    @unittest.skip('Never used')
    def test_str_str(self):
        with recording_activated():
            x = "Hello"
            str(x)
        self.assertTrue(is_recorded(self.recorder, str, '__str__'))

    # Non-dunder methods
    def test_str_capitalize(self):
        with recording_activated():
            x = "hello"
            x.capitalize()
        self.assertTrue(is_recorded(self.recorder, str, 'capitalize'))

    def test_str_casefold(self):
        with recording_activated():
            x = "HELLO"
            x.casefold()
        self.assertTrue(is_recorded(self.recorder, str, 'casefold'))

    def test_str_center(self):
        with recording_activated():
            x = "hello"
            x.center(10)
        self.assertTrue(is_recorded(self.recorder, str, 'center'))

    def test_str_count(self):
        with recording_activated():
            x = "hello"
            x.count('l')
        self.assertTrue(is_recorded(self.recorder, str, 'count'))

    def test_str_endswith(self):
        with recording_activated():
            x = "hello"
            x.endswith("o")
        self.assertTrue(is_recorded(self.recorder, str, 'endswith'))

    def test_str_find(self):
        with recording_activated():
            x = "hello"
            x.find('l')
        self.assertTrue(is_recorded(self.recorder, str, 'find'))

    def test_str_format(self):
        with recording_activated():
            x = "Hello {}"
            x.format("World")
        self.assertTrue(is_recorded(self.recorder, str, 'format'))

    def test_str_index(self):
        with recording_activated():
            x = "hello"
            x.index('e')
        self.assertTrue(is_recorded(self.recorder, str, 'index'))

    def test_str_isalnum(self):
        with recording_activated():
            x = "hello123"
            x.isalnum()
        self.assertTrue(is_recorded(self.recorder, str, 'isalnum'))

    def test_str_isalpha(self):
        with recording_activated():
            x = "hello"
            x.isalpha()
        self.assertTrue(is_recorded(self.recorder, str, 'isalpha'))

    def test_str_isascii(self):
        with recording_activated():
            x = "hello"
            x.isascii()
        self.assertTrue(is_recorded(self.recorder, str, 'isascii'))

    def test_str_isdigit(self):
        with recording_activated():
            x = "123"
            x.isdigit()
        self.assertTrue(is_recorded(self.recorder, str, 'isdigit'))

    def test_str_islower(self):
        with recording_activated():
            x = "hello"
            x.islower()
        self.assertTrue(is_recorded(self.recorder, str, 'islower'))

    def test_str_isnumeric(self):
        with recording_activated():
            x = "123"
            x.isnumeric()
        self.assertTrue(is_recorded(self.recorder, str, 'isnumeric'))

    def test_str_isspace(self):
        with recording_activated():
            x = " "
            x.isspace()
        self.assertTrue(is_recorded(self.recorder, str, 'isspace'))

    def test_str_istitle(self):
        with recording_activated():
            x = "Hello World"
            x.istitle()
        self.assertTrue(is_recorded(self.recorder, str, 'istitle'))

    def test_str_isupper(self):
        with recording_activated():
            x = "HELLO"
            x.isupper()
        self.assertTrue(is_recorded(self.recorder, str, 'isupper'))

    def test_str_join(self):
        with recording_activated():
            x = ", "
            x.join(["Hello", "World"])
        self.assertTrue(is_recorded(self.recorder, str, 'join'))

    def test_str_lower(self):
        with recording_activated():
            x = "HELLO"
            x.lower()
        self.assertTrue(is_recorded(self.recorder, str, 'lower'))

    def test_str_upper(self):
        with recording_activated():
            x = "hello"
            x.upper()
        self.assertTrue(is_recorded(self.recorder, str, 'upper'))

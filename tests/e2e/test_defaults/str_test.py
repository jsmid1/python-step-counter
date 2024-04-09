import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


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
        with RecodingActivated():
            x = "Hello"
            x + " World"
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__add__'))

    def test_str_contains(self):
        with RecodingActivated():
            x = "Hello"
            "H" in x
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__contains__'))

    def test_str_eq(self):
        with RecodingActivated():
            x = "Hello"
            x == "Hello"
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__eq__'))

    def test_str_getitem(self):
        with RecodingActivated():
            x = "Hello"
            x[0]
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__getitem__'))

    def test_str_iter(self):
        with RecodingActivated():
            x = "Hello"
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__iter__'))

    def test_str_len(self):
        with RecodingActivated():
            x = "Hello"
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__len__'))

    @unittest.skip('Creates a new string')
    def test_str_mod(self):
        with RecodingActivated():
            x = "%s World"
            x % "Hello"
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__mod__'))

    def test_str_mul(self):
        with RecodingActivated():
            x = "Hello"
            x * 2
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__mul__'))

    def test_str_ne(self):
        with RecodingActivated():
            x = "Hello"
            x != "World"
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__ne__'))

    @unittest.skip('Never used')
    def test_str_str(self):
        with RecodingActivated():
            x = "Hello"
            str(x)
        self.assertTrue(is_recorded(self.recorder, builtins, str, '__str__'))

    # Non-dunder methods
    def test_str_capitalize(self):
        with RecodingActivated():
            x = "hello"
            x.capitalize()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'capitalize'))

    def test_str_casefold(self):
        with RecodingActivated():
            x = "HELLO"
            x.casefold()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'casefold'))

    def test_str_center(self):
        with RecodingActivated():
            x = "hello"
            x.center(10)
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'center'))

    def test_str_count(self):
        with RecodingActivated():
            x = "hello"
            x.count('l')
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'count'))

    def test_str_endswith(self):
        with RecodingActivated():
            x = "hello"
            x.endswith("o")
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'endswith'))

    def test_str_find(self):
        with RecodingActivated():
            x = "hello"
            x.find('l')
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'find'))

    def test_str_format(self):
        with RecodingActivated():
            x = "Hello {}"
            x.format("World")
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'format'))

    def test_str_index(self):
        with RecodingActivated():
            x = "hello"
            x.index('e')
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'index'))

    def test_str_isalnum(self):
        with RecodingActivated():
            x = "hello123"
            x.isalnum()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isalnum'))

    def test_str_isalpha(self):
        with RecodingActivated():
            x = "hello"
            x.isalpha()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isalpha'))

    def test_str_isascii(self):
        with RecodingActivated():
            x = "hello"
            x.isascii()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isascii'))

    def test_str_isdigit(self):
        with RecodingActivated():
            x = "123"
            x.isdigit()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isdigit'))

    def test_str_islower(self):
        with RecodingActivated():
            x = "hello"
            x.islower()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'islower'))

    def test_str_isnumeric(self):
        with RecodingActivated():
            x = "123"
            x.isnumeric()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isnumeric'))

    def test_str_isspace(self):
        with RecodingActivated():
            x = " "
            x.isspace()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isspace'))

    def test_str_istitle(self):
        with RecodingActivated():
            x = "Hello World"
            x.istitle()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'istitle'))

    def test_str_isupper(self):
        with RecodingActivated():
            x = "HELLO"
            x.isupper()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'isupper'))

    def test_str_join(self):
        with RecodingActivated():
            x = ", "
            x.join(["Hello", "World"])
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'join'))

    def test_str_lower(self):
        with RecodingActivated():
            x = "HELLO"
            x.lower()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'lower'))

    def test_str_upper(self):
        with RecodingActivated():
            x = "hello"
            x.upper()
        self.assertTrue(is_recorded(self.recorder, builtins, str, 'upper'))

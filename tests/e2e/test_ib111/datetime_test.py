import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import datetime


class TestDatetimeMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = sys.modules[__name__]
        cls.recorder, _ = setup_recording(cls.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_date_today_test(self):
        d = datetime.date(1, 2, 3)
        with RecodingActivated():
            d.today()
        self.assertTrue(is_recorded(self.recorder, datetime, datetime.date, 'today'))

    def test_datetime_today_test(self):
        d = datetime.datetime(1, 2, 3)
        with RecodingActivated():
            d.today()
        self.assertTrue(
            is_recorded(self.recorder, datetime, datetime.datetime, 'today')
        )

    def test_time_fromisoformat_test(self):
        t = datetime.time(1, 2, 3)
        with RecodingActivated():
            t.fromisoformat('14:05:15')
        self.assertTrue(
            is_recorded(self.recorder, datetime, datetime.time, 'fromisoformat')
        )

    def test_timedelta_total_seconds_test(self):
        td = datetime.timedelta(1, 2, 3)
        with RecodingActivated():
            td.total_seconds()
        self.assertTrue(
            is_recorded(self.recorder, datetime, datetime.timedelta, 'total_seconds')
        )

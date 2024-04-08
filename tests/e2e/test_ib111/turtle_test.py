import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import turtle


class TestTurtleMethods(unittest.TestCase):
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

    def test_turtle_forward(self):
        with recording_activated():
            turtle.forward(100)
        self.assertTrue(is_recorded(self.recorder, turtle, 'forward'))

    def test_turtle_backward(self):
        with recording_activated():
            turtle.backward(100)
        self.assertTrue(is_recorded(self.recorder, turtle, 'backward'))

    def test_turtle_right(self):
        with recording_activated():
            turtle.right(90)
        self.assertTrue(is_recorded(self.recorder, turtle, 'right'))

    def test_turtle_left(self):
        with recording_activated():
            turtle.left(90)
        self.assertTrue(is_recorded(self.recorder, turtle, 'left'))

    def test_turtle_setheading(self):
        with recording_activated():
            turtle.setheading(180)
        self.assertTrue(is_recorded(self.recorder, turtle, 'setheading'))

    def test_turtle_speed(self):
        with recording_activated():
            turtle.speed(1)
        self.assertTrue(is_recorded(self.recorder, turtle, 'speed'))

    def test_turtle_delay(self):
        with recording_activated():
            turtle.delay(1)
        self.assertTrue(is_recorded(self.recorder, turtle, 'delay'))

    def test_turtle_penup(self):
        with recording_activated():
            turtle.penup()
        self.assertTrue(is_recorded(self.recorder, turtle, 'penup'))

    def test_turtle_pendown(self):
        with recording_activated():
            turtle.pendown()
        self.assertTrue(is_recorded(self.recorder, turtle, 'pendown'))

    @unittest.skip('Skip testing done as its stops the event loop')
    def test_turtle_done(self):
        with recording_activated():
            turtle.done()
        self.assertTrue(is_recorded(self.recorder, turtle, 'done'))

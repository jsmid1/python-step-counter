import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import random


class TestRandomMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = sys.modules[__name__]
        cls.recorder, _ = setup_recording(cls.module, {sys, unittest, sr})

        cls.random_instance = random.Random()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_random_seed(self):
        with RecodingActivated():
            random.seed(42)
        self.assertTrue(is_recorded(self.recorder, random, None, 'seed'))

    def test_random_randint(self):
        with RecodingActivated():
            random.randint(1, 10)
        self.assertTrue(is_recorded(self.recorder, random, None, 'randint'))

    def test_random_random(self):
        with RecodingActivated():
            random.random()
        self.assertTrue(is_recorded(self.recorder, random, None, 'random'))

    def test_random_shuffle(self):
        with RecodingActivated():
            lst = [1, 2, 3, 4]
            random.shuffle(lst)
        self.assertTrue(is_recorded(self.recorder, random, None, 'shuffle'))

    def test_random_choice(self):
        with RecodingActivated():
            choice = random.choice([1, 2, 3, 4])
        self.assertTrue(is_recorded(self.recorder, random, None, 'choice'))

    def test_random_sample(self):
        with RecodingActivated():
            sample = random.sample([1, 2, 3, 4], 2)
        self.assertTrue(is_recorded(self.recorder, random, None, 'sample'))

    # Test for Random class

    def test_random_betavariate(self):
        with RecodingActivated():
            self.random_instance.betavariate(0.9, 0.1)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'betavariate')
        )

    def test_random_choices(self):
        with RecodingActivated():
            self.random_instance.choices([1, 2, 3, 4], k=2)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'choices'))

    def test_random_expovariate(self):
        with RecodingActivated():
            self.random_instance.expovariate(1.5)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'expovariate')
        )

    def test_random_gammavariate(self):
        with RecodingActivated():
            self.random_instance.gammavariate(9.0, 0.5)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'gammavariate')
        )

    def test_random_gauss(self):
        with RecodingActivated():
            self.random_instance.gauss(0, 1)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'gauss'))

    def test_random_getrandbits(self):
        with RecodingActivated():
            self.random_instance.getrandbits(16)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'getrandbits')
        )

    def test_random_getstate(self):
        with RecodingActivated():
            self.random_instance.getstate()
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'getstate'))

    def test_random_lognormvariate(self):
        with RecodingActivated():
            self.random_instance.lognormvariate(0, 1)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'lognormvariate')
        )

    def test_random_normalvariate(self):
        with RecodingActivated():
            self.random_instance.normalvariate(0, 1)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'normalvariate')
        )

    def test_random_paretovariate(self):
        with RecodingActivated():
            self.random_instance.paretovariate(5)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'paretovariate')
        )

    def test_random_randbytes(self):
        with RecodingActivated():
            self.random_instance.randbytes(8)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'randbytes'))

    def test_random_randrange(self):
        with RecodingActivated():
            self.random_instance.randrange(1, 10)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'randrange'))

    def test_random_setstate(self):
        state = self.random_instance.getstate()
        with RecodingActivated():
            self.random_instance.setstate(state)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'setstate'))

    def test_random_triangular(self):
        with RecodingActivated():
            self.random_instance.triangular(1, 10, 5)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'triangular'))

    def test_random_uniform(self):
        with RecodingActivated():
            self.random_instance.uniform(1, 10)
        self.assertTrue(is_recorded(self.recorder, random, random.Random, 'uniform'))

    def test_random_vonmisesvariate(self):
        with RecodingActivated():
            self.random_instance.vonmisesvariate(0, 4)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'vonmisesvariate')
        )

    def test_random_weibullvariate(self):
        with RecodingActivated():
            self.random_instance.weibullvariate(1, 1.5)
        self.assertTrue(
            is_recorded(self.recorder, random, random.Random, 'weibullvariate')
        )

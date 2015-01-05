from twisted.trial import unittest

from collections2 import FrozenOrderedSet


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.s = FrozenOrderedSet('abcdefg')

    def test_order(self):
        expected = list(enumerate('abcdefg'))
        self.assertEquals(list(enumerate(self.s)), expected)

    def test_index(self):
        self.assertEquals(self.s.key_index('c'), 2)

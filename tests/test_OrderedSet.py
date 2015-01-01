from twisted.trial import unittest

from better_od import OrderedSet


class TestOrderedSet(unittest.TestCase):
    def setUp(self):
        self.values = 'abcddefg'
        self.s = OrderedSet(self.values)

    def test_order(self):
        expected = list(enumerate('abcdefg'))
        self.assertEquals(list(enumerate(self.s)), expected)

    def test_index(self):
        self.assertEquals(self.s.key_index('c'), 2)


class TestOrderedSetMutations(unittest.TestCase):
    def test_add_new_value(self):
        prev = len(self.s)
        self.s.add('z')
        self.assertEqual(len(self.s), prev + 1)

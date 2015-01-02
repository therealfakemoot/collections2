from twisted.trial import unittest

from collections2 import OrderedSet


class TestOrderedSet(unittest.TestCase):
    def setUp(self):
        self.s = OrderedSet('abcdefg')

    def test_order(self):
        expected = list(enumerate('abcdefg'))
        self.assertEquals(list(enumerate(self.s)), expected)

    def test_reorder(self):
        new_order = 'gdcbaef'
        self.s.reorder_keys(new_order)
        self.assertEquals(list(enumerate(self.s)), list(enumerate(new_order)))

    def test_index(self):
        self.assertEquals(self.s.key_index('c'), 2)


class TestOrderedSetMutations(unittest.TestCase):
    def test_add_new_value(self):
        s = OrderedSet('abcdef')
        prev = len(s)
        s.add('z')
        self.assertEqual(len(s), prev + 1)

    def test_add_existing_value(self):
        s = OrderedSet('abcdef')
        prev = len(s)
        s.add('a')
        self.assertEqual(len(s), prev)

    def test_discard_existing_value(self):
        s = OrderedSet('abcdef')
        self.assertIs(s.discard('a'), None)

    def test_discard_nonexistent_value(self):
        s = OrderedSet('abcdef')
        self.assertIs(s.discard('z'), None)

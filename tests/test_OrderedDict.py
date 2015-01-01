from twisted.trial import unittest

from better_od import OrderedDict


class TestOrderedDict(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = OrderedDict(zip(self._test_keys, self._test_vals))

    def test_OrderedDict_order(self):
        self.assertEquals(self.d.keys(), [key for key in self._test_keys])

    def test_OrderedDict_index(self):
        self.assertEquals(self.d.key_index('c'), 2)

    def test_OrderedDict_reorder(self):
        new_order = ['c', 'a', 'b']
        self.d.reorder_keys(new_order)
        self.assertEquals(self.d.keys(), new_order)


class TestOrderedDictEquality(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = OrderedDict(zip(self._test_keys, self._test_vals))

    def test_order_check(self):
        bod = OrderedDict([('c', 1), ('b', 0), ('a', -2)])
        self.assertNotEquals(self.d, bod)

    def test_value_check(self):
        bod = OrderedDict([('a', -2), ('b', 0), ('c', 3)])
        self.assertNotEquals(self.d, bod)

    def test_builtin_dict_inequality(self):
        d = {'a': -2, 'b': 0, 'c': 3}
        self.assertNotEquals(self.d, d)

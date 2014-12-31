from twisted.trial import unittest
from twisted.trial.itrial import IReporter

from better_od import BOD


class DocstringReporter(IReporter):
    pass


class TestBOD(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = BOD(zip(self._test_keys, self._test_vals))

    def test_BOD_order(self):
        self.assertEquals(self.d.keys(), [key for key in self._test_keys])

    def test_BOD_index(self):
        self.assertEquals(self.d.key_index('c'), 2)

    def test_BOD_reorder(self):
        new_order = ['c', 'a', 'b']
        self.d.reorder_keys(new_order)
        self.assertEquals(self.d.keys(), new_order)


class TestBODEquality(unittest.TestCase):
    def setUp(self):
        self._test_keys = ['a', 'b', 'c']
        self._test_vals = [-2, 0, 1]
        self.d = BOD(zip(self._test_keys, self._test_vals))

    def test_order_check(self):
        bod = BOD([('c', 1), ('b', 0), ('a', -2)])
        self.assertNotEquals(self.d, bod)

    def test_value_check(self):
        bod = BOD([('a', -2), ('b', 0), ('c', 3)])
        self.assertNotEquals(self.d, bod)

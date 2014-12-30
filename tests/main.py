from better_od import BetterOrderedDict as odict
import pytest


def assert_against_list(d, l):
    assert d.items() == l
    assert d.keys() == [k for k, v in l]
    assert d.values() == [v for k, v in l]
    assert len(d) == len(l)


def test_init():
    base_list = [('a', 'b'),
                 ('c', 'd'),
                 ('e', 'f'),
                 ('g', 'h')]
    d = odict(base_list)
    assert_against_list(d, base_list)


def test_get():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    assert d['a'] == 'b'
    assert d['c'] == 'd'
    assert d['e'] == 'f'
    assert d['g'] == 'h'


def test_key_index():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    assert d.key_index('a') == 0
    assert d.key_index('c') == 1
    assert d.key_index('e') == 2
    assert d.key_index('g') == 3


def test_insert():
    scenario = [(('a', 'b', 2), 0),
                (('c', 'd', 2), 1),
                (('e', 'f', 2), 2),
                (('g', 'h', 2), 2),
                (('i', 'j', 2), 2),
                (('k', 'l', 10), 5),
                (('m', 'n', 4), 4)]

    d = odict()
    for data, result in scenario:
        d.insert(*data)
        assert d[data[0]] == data[1]
        assert d.keys()[result] == data[0]

    assert_against_list(d, [('a', 'b'),
                            ('c', 'd'),
                            ('i', 'j'),
                            ('g', 'h'),
                            ('m', 'n'),
                            ('e', 'f'),
                            ('k', 'l')])


def test_update_with_insert():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    d.insert('c', 'z', 3)

    assert_against_list(d, [('a', 'b'),
                            ('e', 'f'),
                            ('g', 'h'),
                            ('c', 'z')])


def test_update():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    d['c'] = 'z'

    assert_against_list(d, [('a', 'b'),
                            ('c', 'z'),
                            ('e', 'f'),
                            ('g', 'h')])


def test_delete():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    del d['c']

    assert_against_list(d, [('a', 'b'),
                            ('e', 'f'),
                            ('g', 'h')])

    d['c'] = 'z'

    assert_against_list(d, [('a', 'b'),
                            ('e', 'f'),
                            ('g', 'h'),
                            ('c', 'z')])


def test_reorder_keys():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    d.reorder_keys(['e', 'c', 'g', 'a'])

    assert_against_list(d, [('e', 'f'),
                            ('c', 'd'),
                            ('g', 'h'),
                            ('a', 'b')])


def test_reorder_keys_fail():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    with pytest.raises(ValueError):
        d.reorder_keys(['e', 'c', 'g', 'a', 'z'])

    with pytest.raises(ValueError):
        d.reorder_keys(['e', 'c', 'g'])

    with pytest.raises(ValueError):
        d.reorder_keys(['e', 'g', 'a', 'z'])

    with pytest.raises(ValueError):
        d.reorder_keys(['e', 'c', 'a'])

    with pytest.raises(ValueError):
        d.reorder_keys(['e', 'g', 'c', 'a', 'a'])


def test_representation():
    d = odict([('a', 'b'),
               ('c', 'd'),
               ('e', 'f'),
               ('g', 'h')])

    assert str(d) == "[('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]"
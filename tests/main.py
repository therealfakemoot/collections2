from better_od import BetterOrderedDict as odict


def test_insert():
    d = odict()

    d.insert('foo', 'bar', 2)
    assert d['foo'] == 'bar'
    assert d.keys()[0] == 'foo'

    d.insert('a', 'b', 2)
    d.insert('c', 'd', 2)
    d.insert('e', 'f', 2)

    assert d['foo'] == 'bar'
    assert d.keys()[0] == 'foo'

from collections import MutableMapping


class OrderedDict(MutableMapping):
    '''OrderedDict is a mapping object that allows for ordered access
    and insertion of keys. With the exception of the key_index, insert, and
    reorder_keys methods behavior is identical to stock dictionary objects.'''

    def __init__(self, items=None):
        '''OrderedDict accepts an optional iterable of two-tuples
        indicating keys and values.'''

        self._d = dict()
        self._keys = []
        if items is None:
            return
        for key, value in items:
            self[key] = value

    def __len__(self):
        return len(self._d)

    def __iter__(self):
        for key in self._keys:
            yield key

    def __setitem__(self, key, value):
        if key not in self._keys:
            self._keys.append(key)
        self._d[key] = value

    def __getitem__(self, key):
        return self._d[key]

    def __delitem__(self, key):
        self._keys.remove(key)
        del self._d[key]

    def key_index(self, key):
        '''Accepts a parameter, :key:, and returns an integer value
        representing its index in the ordered list of keys.'''
        return self._keys.index(key)

    def insert(self, key, value, index):
        '''Accepts a :key:, :value:, and :index: parameter and inserts
        a new key, value member at the desired index.

        Note: Inserting with a negative index will have the following behavior:
        >>> l = [1, 2, 3, 4]
        >>> l.insert(-1, 5)
        >>> l
        [1, 2, 3, 5, 4]
        '''

        if key in self._keys:
            self._keys.remove(key)
        self._keys.insert(index, key)
        self._d[key] = value

    def reorder_keys(self, keys):
        '''Accepts a :keys: parameter, an iterable of keys in the
        desired new order. The :keys: parameter must contain all
        existing keys.'''
        if len(keys) != len(self._keys):
            raise ValueError('The supplied number of keys does not match.')
        if set(keys) != set(self._d.keys()):
            raise ValueError('The supplied keys do not match the current set of keys.')
        self._keys = keys

    def __repr__(self):
        return str([(key, self[key]) for key in self])

    def __eq__(self, other):
        if not isinstance(other, OrderedDict):
            return False

        return self.items() == other.items()

from collections import MutableMapping


class BetterOrderedDict(MutableMapping):
    '''BetterOrderedDict is a mapping object that allows for ordered access
    and insertion of keys. With the exception of the key_index, insert, and
    reorder_keys methods behavior is identical to stock dictionary objects.'''

    def __init__(self, **kwargs):
        '''BetterOrderedDict accepts an optional iterable of two-tuples
        indicating keys and values.'''

        self._d = dict()
        self._keys = []

    def __len__(self):
        return len(self._d)

    def __iter__(self):
        for key in self._keys:
            yield key

    def __setitem__(self, key, value):
        self._keys.append(key)
        self._d[key] = value

    def __getitem__(self, key):
        return self._d[key]

    def __delitem__(self, key):
        self._keys.pop(key)
        del self._d[key]

    def key_index(self, key):
        '''Accepts a parameter, :key:, and returns an integer value
        representing its index in the ordered list of keys.'''
        return self._keys.index(key)

    def insert(self, key, value, index):
        '''Accepts a :key:, :value:, and :index: parameter and inserts
        a new key, value member at the desired index.'''
        if key in self._d:
            self._keys.pop(key)
        self._keys.insert(index, key)
        self._d[key] = value

    def reorder_keys(self, keys):
        '''Accepts a :keys: parameter, an iterable of keys in the
        desired new order. The :keys: parameter must contain all
        existing keys.'''
        if self._keys != self._d:
            raise ValueError('Keys do not match.')
        self._keys = keys

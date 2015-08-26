from collections import Set, MutableSet


class OrderedSet(MutableSet):
    def __init__(self, items=None):
        if items is None:
            self._set = set()
            self._keys = []
            return
        self._set = set(items)
        self._keys = []
        for key in items:
            if key not in self._keys:
                self._keys.append(key)

    def __contains__(self, value):
        return value in self._set

    def __iter__(self):
        for key in self._keys:
            yield key

    def __len__(self):
        return len(self._set)

    def __repr__(self):
        return str(list(enumerate(self._keys)))

    def add(self, value):
        if value in self._set:
            return
        else:
            self._keys.append(value)
            self._set.add(value)

    def discard(self, value):
        self._set.discard(value)

    def key_index(self, key):
        return self._keys.index(key)

    def insert(self, value, index):
        '''Accepts a :value: and :index: parameter and inserts
        a new key, value member at the desired index.

        Note: Inserting with a negative index will have the following behavior:
        >>> l = [1, 2, 3, 4]
        >>> l.insert(-1, 5)
        >>> l
        [1, 2, 3, 5, 4]
        '''

        if value in self._set:
            self._set.discard(value)
        self._keys.insert(index, value)
        self._set.add(value)

    def reorder_keys(self, keys):
        '''Accepts a :keys: parameter, an iterable of keys in the
        desired new order. The :keys: parameter must contain all
        existing keys.'''
        if len(keys) != len(self._set):
            raise ValueError('The supplied number of keys does not match.')
        if set(keys) != self._set:
            raise ValueError('The supplied keys do not match the current set of keys.')
        self._keys = list(keys)

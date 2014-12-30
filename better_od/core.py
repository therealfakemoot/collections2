from collections import MutableMapping


class BetterOrderedDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._d = dict()
        self._keys = []
        if args:
            if type(args[0]) is list:
                for k, v in args[0]:
                    self[k] = v

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
        return self._keys.index(key)

    def insert(self, key, value, index):
        if key in self._keys:
            self._keys.remove(key)
        self._keys.insert(index, key)
        self._d[key] = value

    def reorder_keys(self, keys):
        if self._keys != self._d:
            raise ValueError('Keys do not match.')
        self._keys = keys

    def __repr__(self):
        return str([(key, self[key]) for key in self])

collections2
=================

#OrderedDict
collections2.OrderedDict is a re-implementation of collections.OrderedDict that allows finer control over the order of its members. It does this by exposing methods for manipulating the internal order-tracking state (a list in the default implementation).

##Usage
The OrderedDict is used identically to other dict-like or mapping objects. The only catch is its constructor doesn't do anything special and can't do smart consumption of dicts versus sequences of tuples and so on. Standard usage is as follows:

##Just a normal dict
```python
>>>from collections2 import OrderedDict
>>>d = OrderedDict()
>>> d['a'] = 1
>>>d['b'] = 2
>>>d
>>>[('a', 1), ('b', 2)]
```

###But predictable
OrderedDict behaves entirely as expected when used as a normal dict, with the exception that iteration will always produce its values in a predictable, controllable manner
```python
>>> for key in d: print d[key]
... 
1
2
>>> d.items()
[('a', 1), ('b', 2)]
>>> d = OrderedDict((('foo', 'bar'), ('something',None)))
>>> d
[('foo', 'bar'), ('something', None)]
```

###Manipulating your OrderedDict for fun and profit
OrderedDict offers several methods for controlling the order it yields values during iteration.
###insert
OrderedDict.insert allows you to insert a key at a given index, letting you manipulate the order of values after object creation or key insertion, a feature which is completely lacking in collections.DefaultDict.

Warning: using an index parameter of -1 with insert() is currently buggy. The recommended workaround is using the order_keys method. Also, adding a new key will add the key to the end of the list, and removing a key and reinserting it as if it were new can be used to accomplish this if desired. 
```python 
>>> d
[('foo', 'bar'), ('something', None)]
>>> d.insert('insert', 'value', 0)
>>> d
[('insert', 'value'), ('foo', 'bar'), ('something', None)]
```

####key_index
OrderedDict.key_index simply returns the integer index of a key in a given BetterOrderedDict. Returns a ValueError if the key does not exist.
```python
>>> d
[('insert', 'value'), ('foo', 'bar'), ('stuff', 'things'), ('something', None)]
>>> d.key_index('insert')
0
```

####reorder_keys
OrderedDict.reorder_keys allows you to completely change the order of all the keys in a BetterOrderedDict by passing an iterable of all existing keys in the new desired ordered.
```python
>>> d
[('insert', 'value'), ('foo', 'bar'), ('stuff', 'things'), ('something', None)]
>>> d.reorder_keys(['foo', 'something', 'stuff', 'insert'])
>>> d
[('foo', 'bar'), ('something', None), ('stuff', 'things'), ('insert', 'value')]
```

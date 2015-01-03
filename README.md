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

#OrderedSet
Like OrderedDict, OrderedSet allows you finer control over the order in which members will appear during iteration.

##Usage
```python
>>> from collections2 import OrderedSet
>>> s = OrderedSet('abcdefg')
>>> s
[(0, 'a'), (1, 'c'), (2, 'b'), (3, 'e'), (4, 'd'), (5, 'g'), (6, 'f')]
>>> 

```
The repr() of OrderedSet objects shows a series of two-tuples, in order, displaying the index and its associated member.
###Iteration
Iteration simply yields the members in order.
``python
>>> for member in s:
...     print member
...     
... 
a
b
c
d
e
f
g
```

###key_index
```python
>>> s
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'e'), (4, 'd'), (5, 'f')]
>>> s.key_index('f')
5
```

###reorder_keys
```python
>>> s.reorder_keys('fadbec')
>>> s
[(0, 'f'), (1, 'a'), (2, 'd'), (3, 'b'), (4, 'e'), (5, 'c')]
```

###insert
```python
>>> s = OrderedSet('abcedf')
>>> s.insert('z', 0)
>>> s
[(0, 'z'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'e'), (5, 'd'), (6, 'f')]
```

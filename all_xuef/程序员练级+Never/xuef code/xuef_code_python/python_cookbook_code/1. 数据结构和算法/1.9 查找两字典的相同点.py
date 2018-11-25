
"""
问题
怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？
"""
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# python3 的 keys()
"""
一个字典就是一个键集合与值集合的映射关系。 字典的 keys() 方法返回一个展现键集合的键视图对象。
键视图的一个很少被了解的特性就是它们也支持集合操作，比如集合并、交、差运算。
"""
# Find keys in common
"""
help(dict.keys)
python3 ok, not python2
"""
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }


"""
这些操作也可以用于修改或者过滤字典元素。
比如，假如你想以现有字典构造一个排除几个指定键的新字典。
下面利用字典推导来实现这样的需求：
"""
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}



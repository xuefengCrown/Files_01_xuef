

"""
抽象基类不能实例化(类似于接口)
1. 强制子类必须实现某方法(强制规定)
比如写web框架时，集成Cache(redis,cache, memorycache)
需要设计一个抽象基类(CacheBase),强制子类必须实现某些方法

比如写爬虫框架时，需要将数据写入数据库或者文件或者kafuk的管道中。
我们也需要设计一个基类，这样用户才能制定不同的写出规则。

这样，只要用户遵守了我们基类中的约定，就可以通过配置来定制不同的服务。
这在我们写一些可扩展的项目或框架时需要考虑的！！！

"""
#from collections.abc import Sized

import collections.abc

print(dir(collections.abc))
"""
['AsyncGenerator', 'AsyncIterable', 'AsyncIterator', 'Awaitable', 'ByteString', 'Callable',
'Collection', 'Container', 'Coroutine', 'Generator', 'Hashable', 'ItemsView', 'Iterable',
'Iterator', 'KeysView', 'Mapping', 'MappingView', 'MutableMapping', 'MutableSequence',
'MutableSet', 'Reversible', 'Sequence', 'Set', 'Sized', 'ValuesView', '__all__',
'__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '
__package__', '__spec__']

"""
##collectons.abc中实现了很多抽象基类(Iterable, Callable, Mutable...)
##它们可以帮助我们理解Python中的继承关系以及一些接口的定义。
##搞清楚这些，我们才能知道比如 dict 的每个方法都是来自哪里的

# 如何实现抽象基类
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, val):
        pass

class RedisCache(CacheBase):
    pass







"""
__delattr__:
__dir__:
__doc__:
__class__: 实例所属的类
__dict__: 实例自定义属性
__eq__:
__ge__:
__gt__:
__le__:
__lt__:
__ne__:
__format__:
__getatribute__: 属性访问拦截
__hash__:
__module__:
__new__:
__init__:
__reduce__:
__reduce_ex__:
__repr__:
__setattr__:
__sizeof__:
__str__:
__subclasshook__:
__weakref__:
"""
class T:
    """ T doc """
    def __init__(self, name=None):
        self.name=name if name else "Rose"
        
p=print

t=T()
#p(str.__dict__)
p(t.__dict__)
n=1
#p(n.__class__)
#p(n.__str__)
#p(dir.__doc__)
#p(help.__doc__)
#p(t.__doc__)
#p(help(t))











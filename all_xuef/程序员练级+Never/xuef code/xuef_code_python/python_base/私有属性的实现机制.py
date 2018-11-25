

class Person:
    """ This is Person __doc__ """
    def __init__(self, name):
        self.__name = name
    

p=Person("xuef")
#print(p.__name) # AttributeError: 'Person' object has no attribute '__name'

# __name 被重整为 _Person__name
print(p._Person__name)

print(p.__dict__)
print(Person.__dict__)
"""
{
'__module__': '__main__',
'__init__': <function Person.__init__ at 0x03117F60>,
'__dict__': <attribute '__dict__' of 'Person' objects>,
'__weakref__': <attribute '__weakref__' of 'Person' objects>,
'__doc__': None}
"""

"""
魔法属性

__call__ : obj() 时调用
__doc__
__init__
__class__
__module__
__del__
__str__ 
__repr__

__getitem__
__setitem__

__getslice__
__setslice__
"""

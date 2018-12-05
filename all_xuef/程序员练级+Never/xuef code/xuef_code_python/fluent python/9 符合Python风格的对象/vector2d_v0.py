
from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    @property
    def x(self): 
        return self.__x
    
    @property 
    def y(self):
        return self.__y
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def angle(self):
        return math.atan2(self.y, self.x)
    # 现在能计算极坐标了
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'): 
            fmt_spec = fmt_spec[:-1] 
            coords = (abs(self), self.angle()) 
            outer_fmt = '<{}, {}>' 
        else:
            coords = self 
            outer_fmt = '({}, {})' 
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components) 

##    为了把 Vector2d 实例变成可散列的，必须使用 __hash__ 方法
##    （还需要 __eq__ 方法，前面已经实现了）
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

v1 = Vector2d(3, 4)
v1.x=5
#如果类没有定义 __format__ 方法，从 object 继承的方法会返回str(my_object)。
print(format(v1, 'p'))



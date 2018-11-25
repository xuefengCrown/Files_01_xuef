
"""
问题
你想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值。
"""

def spam(a, b=42):
    print(a, b)

spam(1) # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

# Using a list as a default value
def spam(a, b=None):
    if b is None:
        b = []

"""
其次，默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串。 特别的，千万不要像下面这样写代码：

def spam(a, b=[]): # NO!
    ...
"""

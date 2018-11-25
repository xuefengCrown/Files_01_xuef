
"""
装饰器在前端中的应用

"""

def makeBold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped

def makeItalic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@makeBold
def m1():
    return "hello, world 1"

@makeItalic
def m2():
    return "hello, world 2"

@makeBold
@makeItalic
def m3():
    return "hello, world 3"

print(m1())
print(m3())

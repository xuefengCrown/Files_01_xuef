"""流模拟
"""

def cons(x, y):
    return x,y
def car(x):
    return x[0]
def cdr(x):
    return x[1:]
def cons_stream(x, y):
    return cons(x, delay(y))

def delay(x):
    pass
 

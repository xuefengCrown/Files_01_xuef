"""
使用自定义序对 pair 来表示一个有理数
"""
from gcd import gcd

# pair 竟然只是一个过程
# 这也说明可以将过程作为对象来对待
def pair(n, d):
    def dispatch(message):
        if message == 0: return n
        if message == 1: return d
        raise ValueError("Argument not 0 or 1")
    return dispatch
def car(p):
    return p(0)
def cdr(p):
    return p(1)

def make_rat(n, d):
    g = gcd(n, d)
    return pair(n//g, d//g)
def numer(x):
    return car(x)
def denom(x):
    return cdr(x)
def print_rat(x):
    print(str(car(x)) + '/' + str(cdr(x)))
    

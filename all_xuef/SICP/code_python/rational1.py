"""
使用tuple来表示有理数
"""
from gcd import gcd

def make_rat(n, d):
    g = gcd(n, d)
    return (n//g, d//g)
def numer(x):
    return x[0]
def denom(x):
    return x[1]
def print_rat(x):
    print(str(x[0]) + '/' + str(x[1]))

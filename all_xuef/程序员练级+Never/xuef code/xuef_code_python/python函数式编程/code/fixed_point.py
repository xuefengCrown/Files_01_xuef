
import time
def next_(n, x):
    return (x+n/x)/2

def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

f = lambda x: next_(5, x)
g = repeat(f, 1.0)
for v in g:
    time.sleep(0.5)
    print(v)

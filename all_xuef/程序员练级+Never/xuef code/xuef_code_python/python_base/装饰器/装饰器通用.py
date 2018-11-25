


def wrap(func):
    def wrapped(*args, **kwargs):
        print('log[', func.__name__, '执行了| 参数为:', args, kwargs, sep='')
        res = func(*args, **kwargs)
        return res
    return wrapped

@wrap
def m1(a, b):
    return a + b

@wrap
def m2(*args):
    return sum(args)

print(m1(1,2))

print(m2(1,2,3,4,5))

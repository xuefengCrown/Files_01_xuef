
from functools import wraps

def logit(logfile='out.log'): # return a decorator
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open('out.log', 'at') as f:
                print("{func} was called...".format(func=func.__name__), file=f)
            return func(*args, **kwargs)
        return wrapper
    return deco


r1 = logit()(sum)(range(20))
r2 = logit()(sum)(range(100))

print(r1, r2)

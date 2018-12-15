
"""
本节再次探讨 clock 装饰器，为它添加一个功能：让用户传入一个格
式字符串，控制被装饰函数的输出。
"""

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func): 
        def clocked(*_args): 
            t0 = time.time()
            _result = func(*_args) 
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result) 
            print(fmt.format(**locals()))
            return _result 
        return clocked 
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)





#coro_exc_demo.py：学习在协程中处理异常的测试代码

class DemoException(Exception):
"""为这次演示定义的异常类型。"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))

    #最后一行代码不会执行，因为只有未处理的异常才会中止那个无限循环，
    #而一旦出现未处理的异常，协程会立即终止。
    raise RuntimeError('This line should never run.')

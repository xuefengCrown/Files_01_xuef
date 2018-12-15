#!/usr/bin/env python3

# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_ASYNCIO
import asyncio
import itertools
import sys


@asyncio.coroutine  # <1>打算交给 asyncio 处理的协程要使用 @asyncio.coroutine 装饰。
def spin(msg):  # <2>这里不需要18-1 中 spin 函数中用来关闭线程的 signal 参数。
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # <3>这样的休眠不会阻塞事件循环。
        except asyncio.CancelledError:  # <4>
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # <5>
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)  # <6>表达式把控制权交给主循环，在休眠结束后恢复这个协程。
    return 42


@asyncio.coroutine
def supervisor():  # <7>supervisor 函数也是协程，因此可以使用 yield from 驱动slow_function 函数。
    spinner = asyncio.async(spin('thinking!'))  # <8>
    print('spinner object:', spinner)  # <9>
    result = yield from slow_function()
    # <10>驱动 slow_function() 函数。结束后，获取返回值。
    # 同时，事件循环继续运行，因为 slow_function 函数最后使用 yield from
    # asyncio.sleep(3) 表达式把控制权交回给了主循环。

    spinner.cancel()  # <11>
    return result


def main():
    loop = asyncio.get_event_loop()  # <12>
    result = loop.run_until_complete(supervisor())  # <13> 驱动 supervisor 协程，让它运行完毕
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_ASYNCIO


"""
协程自身就会同步，因为在任意时刻只有一个协程运行。想交出
控制权时，可以使用 yield 或 yield from 把控制权交还调度程序。
"""

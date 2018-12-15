
import asyncio, threading

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(2) # 函数会悬停在这里
    print('Hello again! (%s)' % threading.currentThread())
    
# 获取EventLoop:
loop = asyncio.get_event_loop()

tasks = [hello(), hello()]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
    
# 分析

## 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

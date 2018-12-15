
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    
    # 异步调用asyncio.sleep(1):
    # 把asyncio.sleep(5)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
    # 而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    r = yield from asyncio.sleep(5) # 函数会悬停在这里
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
    

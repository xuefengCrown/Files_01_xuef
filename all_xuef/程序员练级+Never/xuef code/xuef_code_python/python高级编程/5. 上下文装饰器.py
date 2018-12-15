
# 上下文装饰器用来确保函数可以运行在正确的上下文中，或者在函数前后执行一些代码。
# 换句话说，它用来设置或复位特定的执行环境。

# 例如，当一个数据项必须与其他线程贡献时，就需要使用一个锁来确保它在多重访问时得到保护。
# 这个锁可以在一个装饰器中编写。

from threading import RLock # 可重入锁

lock = RLock()

def sync(func):
    def _sync(*args, **kw):
        lock.acquire()
        try:
            return func(*args, **kw)
        finally:
            lock.release()
    return _sync

# 上下文装饰器可以使用 with 语句来代替

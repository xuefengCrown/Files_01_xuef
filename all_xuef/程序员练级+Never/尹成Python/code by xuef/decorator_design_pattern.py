
"""
装饰器模式实现测试函数运行时间的通用模板
"""
import time

def runtime(func):
    start = time.time()
    func()
    end = time.time()
    last_time = end - start
    print(func.__name__ + " 的运行时间为:", format(last_time, ".2f"), "秒")

def test():
    sam = 0
    for i in range(1, 10000000):
        sam += i
    print("sam:", sam)

runtime(test)

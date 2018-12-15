# http://www.dabeaz.com/coroutines/Coroutines.pdf
"""
Python中的协程和生成器很相似但又稍有不同。
"""
# 主要区别在于：生成器是数据的生产者，协程则是数据的消费者

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print("[*]", line) 

search = grep('coroutine')
next(search) # 预激协程
#output: Searching for coroutine

search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")

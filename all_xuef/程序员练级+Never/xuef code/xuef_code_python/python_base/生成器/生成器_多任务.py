
"""
协程
"""

def task1():
    while True:
        print("task 1")
        yield None

def task2():
    while True:
        print("task 2")
        yield None


t1 = task1()
t2 = task2()
while True:
    t1.__next__()
    t2.__next__()
    

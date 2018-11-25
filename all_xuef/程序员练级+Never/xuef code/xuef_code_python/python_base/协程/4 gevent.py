import gevent,time
from gevent import monkey

"""
开多线程时monkey会阻塞住线程的继续执行，需要对monkey.patch_all进行处理，解决方案有2种： 
1. monkey.patch_all(thread=False) 
2. 直接用gevent.sleep()
"""
monkey.patch_all(thread=False)

def task1():
    while 1:
        print("task 1...", gevent.getcurrent())
        time.sleep(0.5)
        
def task2():
    while 1:
        print("task 2...", gevent.getcurrent())
        time.sleep(0.5)

gr1 = gevent.spawn(task1)
gr2 = gevent.spawn(task2)

##gr1.join()
##gr2.join()
gevent.joinall([gr1, gr2])

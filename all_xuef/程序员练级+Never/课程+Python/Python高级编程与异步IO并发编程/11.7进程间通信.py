
# 1. 全局变量不适用于多进程间，因为创建进程会拷贝数据后执行。

# 2. 各种 Queue 通信
from queue import Queue # 线程间
from multiprocessing import Queue # 进程间

from multiprocessing import Manager # Manager().Queue() pool的进程池

# 3. 使用Pipe通信
from multiprocessing import Pipe
# Pipe 只适用于两个指定进程间通信
recv_pipe, send_pipe = Pipe()

my_producer = Processs(target=producer, args=(send_pipe)) # pipe.send("hello")
my_consumer = Processs(target=consumer, args=(recv_pipe)) # pipe.recv()

# 4. 如何在多个进程间维护一个公共的内存模块？(共享内存)
pro_shared_dict = Manager().dict() # 线程的那一套数据结构和同步机制，Manager中有相应的一套

# !!! 使用时要注意同步，使用 RLock(可重入锁), Semaphore(信号量), Condition




















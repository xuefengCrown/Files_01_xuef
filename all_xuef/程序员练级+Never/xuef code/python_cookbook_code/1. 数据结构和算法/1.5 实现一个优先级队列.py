
"""

问题
怎样实现一个按优先级排序的队列？
并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
"""

# TODO 如果你想在多个线程中使用同一个队列，那么你需要增加适当的锁和信号量机制。
# 可以查看 12.3 小节的例子演示是怎样做的。
"""
heapq 介绍
    heap = [] #创建了一个空堆 
    heappush(heap,item) #往堆中插入一条新的值 
    item = heappop(heap) #从堆中弹出最小值 
    item = heap[0] #查看堆中最小值，不弹出 


"""

# 下面的类利用 heapq 模块实现了一个简单的优先级队列
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        # index 变量的作用是保证同等优先级元素的正确排序。
        # 不可能有两个元素有相同的 index 值
        self._index = 0 

    def push(self, item, priority):
        # 元组在比较大小的时候，首先比较第一个元素，如果能够判断那么就直接根据第一个元素进行判断，
        # 如果不能，就取下一个元素进行判断，依次类推。直到比较出结果或者一方没有元素了。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1 # 元素的插入顺序

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def test():
    q = PriorityQueue()
    q.push("QQ", 10)
    q.push("notepad", 5)
    q.push("notepad", 5)
    q.push("chrome", 7)

    for i in range(4):
        print(q.pop())

test()
        

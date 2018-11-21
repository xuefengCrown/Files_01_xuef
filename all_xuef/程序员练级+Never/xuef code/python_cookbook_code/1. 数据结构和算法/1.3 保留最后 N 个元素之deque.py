

"""
历史记录命令
"""
from collections import deque

history = 5
previouss = deque(maxlen=history)

for i in range(1,6):
    previouss.append(i)
# deque([1, 2, 3, 4, 5], maxlen=5)

print(previouss)
previouss.appendleft(6)
print(previouss)
previouss.pop()
print(previouss)

"""
更一般的， deque 类可以被用在任何你只需要一个简单队列数据结构的场合。
如果你不设置最大队列大小，那么就会得到一个无限大小队列，
你可以在队列的两端执行添加和弹出元素的操作。
"""

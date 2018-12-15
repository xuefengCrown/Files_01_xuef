
"""
栈帧对象存在于堆内存中，这意味着栈帧可以独立于调用者而存在。
"""

def foo():
    bar()

def bar():
    pass

import dis

print(dis.dis(foo))

"""
cd C:\python36\Scripts
pip3.6 install greenlet

"""

import greenlet as gl
import time

def task1():
    while 1:
        print("task 1...")
        gr2.switch()
        time.sleep(0.5)
def task2():
    while 1:
        print("task 2...")
        gr1.switch()
        time.sleep(0.5)

gr1 = gl.greenlet(task1)
gr2 = gl.greenlet(task2)

gr1.switch()

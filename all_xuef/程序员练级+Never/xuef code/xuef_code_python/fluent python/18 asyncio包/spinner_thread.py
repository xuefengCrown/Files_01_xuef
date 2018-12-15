#coding: utf-8
#!/usr/bin/env python2.7

# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_THREAD
import threading
import itertools
import time
import sys

DELAY = 0.1

"""
注意，Python 没有提供终止线程的 API，这是有意为之的。若想关闭线
程，必须给线程发送消息。这里，我使用的是 signal.go 属性：在主
线程中把它设为 False 后，spinner 线程最终会注意到，然后干净地
退出
"""
class Signal: #信号,用于从外部控制线程。
    go = True 
    
def spin(msg, signal):  # <2>这个函数会在单独的线程中运行。
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # <3>
        status = char + ' ' + msg
        write(status)
        flush()
        ##显示文本式动画的诀窍所在：使用退格符（\x08）把光标移回来。
        write('\x08' * len(status))  # <4>
        time.sleep(DELAY)
        if not signal.go:  # <5>
            break
    
    write(' ' * len(status) + '\x08' * len(status))  # <6>使用空格清除状态消息，把光标移回开头。


def slow_function():  # <7>
    # pretend waiting a long time for I/O
    #调用 sleep 函数会阻塞主线程，不过一定要这么做，以便释放GIL，创建从属线程。
    time.sleep(3)  # <8>
    return 42


def main():
    #设置从属线程，显示线程对象，运行耗时的计算，最后杀死线程。
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print 'spinner object:', spinner  # <10>
    spinner.start()  # <11>

    #运行 slow_function 函数，阻塞主线程。同时，从属线程以动画形式显示旋转指针。
    result = slow_function()  # <12>
    signal.go = False  # <13> 线程由os调度,所以我们无法精确知道这一步何时会执行
    spinner.join()  # <14>等待 spinner 线程结束。
    
    print 'Answer:', result


if __name__ == '__main__':
    main()
# END SPINNER_THREAD

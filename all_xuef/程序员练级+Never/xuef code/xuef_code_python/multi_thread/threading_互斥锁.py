
import time
import threading

num=0
mutex = threading.Lock()
def adder1():
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
    print("adder1 num=", num)
def adder2():
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
    print("adder2 num=", num)
def main():
    t1 = threading.Thread(target=adder1)
    t2 = threading.Thread(target=adder2)
    t1.start()
    t2.start()
    time.sleep(10)
    print("main thread, num=", num)
# 程序停止不了???
if __name__ == "__main__":
    main()

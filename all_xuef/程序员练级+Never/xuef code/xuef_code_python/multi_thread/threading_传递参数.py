
import time
import threading

num=0
def adder1(a, b):
    print('adder1 a=',a,'adder1 b=',b)
    global num
    for i in range(a*b):
        num += 1
def adder2(a):
    print('adder2 a=',a)
    global num
    for i in range(a):
        num += 1

def main():
    t1 = threading.Thread(target=adder1, args=(200,10000))
    t2 = threading.Thread(target=adder2, args=(2000000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("main thread, num=", num)
# 程序停止不了???
if __name__ == "__main__":
    main()

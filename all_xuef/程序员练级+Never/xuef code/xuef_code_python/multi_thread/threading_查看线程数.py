
import time
import threading

def sing():
    for i in range(5):
        print("singing...", i)
        time.sleep(1)

def dance():
    for i in range(5):
        print("dancing...", i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while 1:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)
# 程序停止不了???
if __name__ == "__main__":
    main()

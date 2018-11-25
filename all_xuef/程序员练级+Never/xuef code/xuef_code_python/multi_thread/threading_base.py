
import time
import threading

def sing():
    for i in range(5):
        print("singing...")
        time.sleep(1)

def dance():
    for i in range(5):
        print("dancing...")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
# 程序停止不了???
if __name__ == "__main__":
    main()


import time
import threading

def task1():
    print("task1 start...")
    time.sleep(2)
    print("task1 end...")

def task2():
    print("task2 start...")
    time.sleep(4)
    print("task2 end...")

def main():
    start_t = time.time()
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    #t2.setDaemon(True)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("run {t} s".format(t=time.time()-start_t))
    
if __name__ == '__main__':
    main()


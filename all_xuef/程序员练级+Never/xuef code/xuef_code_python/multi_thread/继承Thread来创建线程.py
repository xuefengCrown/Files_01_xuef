
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(20):
            print(i)


def main():
    t = MyThread()
    t.start()

if __name__ == '__main__':
    main()
    

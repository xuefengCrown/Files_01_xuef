
# 对于计算密集型(耗cpu)，多进程优于多线程
import time

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n<2:
        return n
    else:
        return fib(n-2) + fib(n-1)

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (n)) for n in range(25,35)]
        start_t = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time()-start_t))


# 对于 IO密集型，多线程要优一点。(sleep来模拟IO操作)


























        


























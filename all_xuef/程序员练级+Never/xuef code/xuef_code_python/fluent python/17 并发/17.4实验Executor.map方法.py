
"""
Experiment with ``ThreadPoolExecutor.map``
"""
# BEGIN EXECUTOR_MAP
from time import sleep, strftime
from concurrent import futures

#把传入的参数打印出来，并在前面加上[HH:MM:SS] 格式的时间戳。
def display(*args):  # <1>
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):  # <2>
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10  # <3>


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # <4>

    #executor.map 方法返回的结果（results）是生成器
    results = executor.map(loiter, range(5))  # <5>
    display('results:', results)  # <6>.
    display('Waiting for individual results:')
    for i, result in enumerate(results):  # <7>
        display('result {}: {}'.format(i, result))


main()

"""
executor.submit 和 futures.as_completed 这个组合比
executor.map 更灵活，因为 submit 方法能处理不同的可调用对
象和参数，而 executor.map 只能处理参数不同的同一个可调用对
象。
"""







# END EXECUTOR_MAP

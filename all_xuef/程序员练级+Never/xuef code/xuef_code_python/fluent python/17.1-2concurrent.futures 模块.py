#17.1.2　使用concurrent.futures模块下载
"""
concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和ProcessPoolExecutor 类，
这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。
这两个类在内部维护着一个工作线程或进程池，以及要执行的任务队列。
不过，这个接口抽象的层级很高，像下载国旗这种简单的案例，无需关心任何实现细节。


严格来说，我们目前测试的并发脚本都不能并行下载。
使用concurrent.futures 库实现的那两个示例受 GIL（Global Interpreter
Lock，全局解释器锁）的限制，而 flags_asyncio.py 脚本在单个线程中运
行。
读到这里，你可能会对前面做的非正规基准测试有下述疑问。
既然 Python 线程受 GIL 的限制，任何时候都只允许运行一个线程，
那么 flags_threadpool.py 脚本的下载速度怎么会比 flags.py 脚本快 5
倍？
"""


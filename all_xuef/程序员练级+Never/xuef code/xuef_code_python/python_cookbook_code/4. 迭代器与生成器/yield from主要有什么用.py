

将yield from视为提供了一个调用者和子生成器之间的透明的双向通道。
包括从子生成器获取数据以及向子生成器传送数据。

为了帮助读者更好理解向生成器send数据的意思，答主建议读者先去阅读协程的相关知识，链接如下：
Dave Beazley's Curious Course on Couroutines
Dave Beazley 协程教程的PPT，更简洁！
1. 利用yield from从生成器读取数据
def reader():
    # 模拟从文件读取数据的生成器
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper(g):
    # 循环迭代从reader产生的数据 
    for v in g:
        yield v

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)

# 结果：
<< 0
<< 1
<< 2
<< 3
我们可以用yield from语句替代reader_wrapper(g)函数中的循环，如下：
def reader_wrapper(g):
    yield from g
效果一样，且代码更简洁有没有。
2.利用yield from语句向生成器（协程）传送数据 
首先创建一个生成器writer，接收传送给它的数据，并写进套接字，文件等；
def writer():
    # 读取send传进的数据，并模拟写进套接字或文件
    while True:
        w = (yield)    # w接收send传进的数据
        print('>> ', w)
现在的问题是，包装器函数如何传送数据给writer函数，使得传递给包装器的数据都能够
显示地传递给writer函数？！
即我们期待得到如下结果：
def writer_wrapper(coro):
    # TBD
    pass

w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # 生成器准备好接收数据
for i in range(4):
    wrap.send(i)

# 期望结果：
>>  0
>>  1
>>  2
>>  3
很显然，包装区需要接收数据并显示传递给生成器，并且需要处理for循环耗尽是生成器产生的StopIteration异常，显然包装器只用for循环已经不能满足需求，满足情况的一般版本如下：
def writer_wrapper(coro1):
    coro1.send(None)  # 生成器准备好接收数据
    while True:
        try:
            x = (yield)  # x接收send传进的数据
            coro1.send(x)  # 然后将x在send给writer子生成器
        except StopIteration:    # 处理子生成器返回的异常
            pass
包装器也是个生成器，上面所有复杂的写法也可以用yield from替换：
def writer_wrapper(coro2):
    yield from coro2
一下子少了好多代码，是不是见证了奇迹！
3. 利用yield from向生成器传送数据--处理异常 更进一步，如果我们的子生成器即writer需要处理异常该怎么办？假设writer需要处理SpamException异常，遇到这个异常打印***，代码如下：
class SpamException(Exception):
    pass

def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)
如果使用上一个一般版本的包装器writer_wrapper(coro1)，会有什么结果？试验如下：
w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # "prime" the coroutine
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)

# 期望结果：
>>  0
>>  1
>>  2
***
>>  4

# 实际结果：
>>  0
>>  1
>>  2
Traceback (most recent call last):
  File ... in <module>
    wrap.throw(SpamException)
  File ... in writer_wrapper
    x = (yield)
__main__.SpamException
可以看出，这行不通，因为x = (yield)语句仅能够引发异常，然后停止运行。我们可以手工在包装器writer_wrapper(coro1)中添加异常处理，并传递或者抛出异常给子生成器writer，代码如下：
def writer_wrapper(coro1):
    # 手工处理异常被抛给子生成器
    coro1.send(None)    # 生成器准备好接收数据
    while True:
        try:
            try:
                x = (yield)
            except Exception as e:   # 捕获异常
                coro1.throw(e)
            else:
                coro1.send(x)
        except StopIteration:
            pass
同样的，这一堆复杂的代码，也可以用yield from语句替换，并且功能完全一样！！！
def writer_wrapper(coro):
    yield from coro
重要的代码贴三遍！三遍！三遍！
看到这里，大概能理解yield from显示处理传值给子生成器以及抛出异常给子生成器的意思了吧。
当然yield from不仅有这两个处理情况，还有之前我们提到的：外部生成器关闭，子生成器也会关闭；子生成器返回一个值得情况（上文第二个代码例子），等等。
总之，这是一个魔法语句，它也是协程的重要组成部分，至于协程，还需要继续学习。

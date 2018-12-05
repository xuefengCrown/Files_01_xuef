"""
https://blog.csdn.net/lanchunhui/article/details/70160295
"""
# 数据读写不一定是文件，也可以在内存中进行。
# StringIO 顾名思义就是在内存中以 io 流的方式读写 str。

from io import StringIO
f = StringIO()

p=print
r=f.write('hello')            # 返回 5，也即写入的字符数目
p(r)
f.write(' ')
f.write('world!')

r=f.getvalue()                # hello world!
p(r)

p("-"*20)
f = StringIO('Hello!\nWorld!')
while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())

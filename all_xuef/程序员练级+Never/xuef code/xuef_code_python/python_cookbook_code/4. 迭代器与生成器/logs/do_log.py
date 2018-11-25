import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    for filename in filenames:
        if filename.endswith(".gz"):
            f = gzip.open(filename, "rt")
        elif filename.endswith(".bz2"):
            f = bz2.open(filename, "rt")
        else:
            #print("------",filename)
            f = open(filename, "rt")
        yield f
        f.close()

def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence.
    """
    for it in iterators:
        #yield from it 简单的返回生成器 it 所产生的所有值。
        #yield from it # iter file-->lines
        for line in it:
            yield line

def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

import pdb
##lst = list(os.walk('.'))
##print(lst)
lognames = gen_find('access-log*', '.')
#print(list(lognames))
#pdb.set_trace()
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)ply', lines)
for line in pylines:
    print(line)

# 以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询等。
"""
为了理解上述代码，重点是要明白 yield 语句作为数据的生产者而 for 循环语句作为数据的消费者。
当这些生成器被连在一起后，每个 yield 会将一个单独的数据元素传递给迭代处理管道的下一阶段。
"""

"""
这种方式一个非常好的特点是每个生成器函数很小并且都是独立的。这样的话就很容易编写和维护它们了。
很多时候，这些函数如果比较通用的话可以在其他场景重复使用。 并且最终将这些组件组合起来的代码看
上去非常简单，也很容易理解。

使用这种方式的内存效率也不得不提。上述代码即便是在一个超大型文件目录中也能工作的很好。
事实上，由于使用了迭代方式处理，代码运行过程中只需要很小很小的内存。
"""

"""
最后还有一点需要注意的是，管道方式并不是万能的。 有时候你想立即处理所有数据。
然而，即便是这种情况，使用生成器管道也可以将这类问题从逻辑上变为工作流的处理方式。
"""

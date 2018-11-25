from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            #yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用。
            yield from flatten(item) #yield from 就会返回所有子例程的值。
##            for i in flatten(item):
##                yield i
        else:
            yield item


items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
p=print
for x in flatten(items):
    p(x,end=" ")

"""
最后要注意的一点是， yield from 在涉及到基于协程和生成器的并发编程中扮演着更加重要的角色。
可以参考12.12小节查看另外一个例子。
"""

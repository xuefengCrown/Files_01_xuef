"""
对表的映射(把皮鞋都拿出来擦一遍)
一种特别有用的操作是将某种变换应用于一个表的所有元素，得到所有结果构成的表。

我们可以抽象出这一具有一般性的想法，将其中的公共模式表述为一个
高阶过程，这一高阶过程称为map。
"""

def xmap(proc, xlist):
    if len(xlist) == 0: return []
    return [proc(xlist[0])] + (xmap(proc, xlist[1:]))
    # 效率会很低。python 的list是用array实现的
    # lisp中这样做很自然，因为它cons出的序列，其底层是linkedlist
    # 既然python没有将LinkedList作为其基本实现，那么这里自己实现的就不值得了。
    # python已经提供了 map，不过我不知道它是怎么实现的。
    
x = [-1, -2, -3]
print(xmap(abs, x))
print(list(map(abs, x)))

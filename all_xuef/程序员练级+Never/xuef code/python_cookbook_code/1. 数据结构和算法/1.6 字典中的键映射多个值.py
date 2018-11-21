"""
问题
怎样实现一个键对应多个值的字典（也叫 multidict）？

解决方案
一个字典就是一个键对应一个单值的映射。
如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。
比如，你可以像下面这样构造这样的字典：

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

"""

"""
选择使用列表还是集合取决于你的实际需求。
如果你想保持元素的插入顺序就应该使用列表，
如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）。
"""

"""
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，
所以你只需要关注添加元素操作了。比如：
"""

from collections import defaultdict

d = defaultdict(list) # list 表示值类型
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

##d = defaultdict(list)
##for key, value in pairs:
##    d[key].append(value)




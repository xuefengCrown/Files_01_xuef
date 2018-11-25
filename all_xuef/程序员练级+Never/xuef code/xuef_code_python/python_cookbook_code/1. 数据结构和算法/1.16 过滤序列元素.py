
"""
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
"""
# 解决方案

## 列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
filtered = [n for n in mylist if n > 0]
print(filtered)

## 生成器表达式
"""
使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。比如：
"""
pos = (n for n in mylist if n > 0)

## filter
"""
有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来。
比如，假设过滤的时候需要处理一些异常或者其他复杂情况。
这时候你可以将过滤代码放到一个函数中， 然后使用内建的 filter() 函数。示例如下：
"""
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']

# filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例那样使用 list() 去转换。


# 另外一个值得关注的过滤工具就是 itertools.compress()
"""
它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
然后输出 iterable 对象中对应选择器为 True 的元素。
当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的。
"""
import itertools
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# 现在你想将那些对应 count 值大于5的地址全部输出
more5 = [n > 5 for n in counts] # Bool 序列
res = itertools.compress(addresses, more5)
print(list(res))



data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data


"""
实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
包括字符串，文件对象，迭代器和生成器
"""
s = 'Hello'
a, b, c, d, e = s


# 1.2 解压可迭代对象赋值给多个变量
"""
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
那么怎样才能从这个可迭代对象中解压出N个元素出来？

解决方案
Python的星号表达式可以用来解决这个问题。
比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有24个呢？这时候星号表达式就派上用场了：

"""

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

first, *middle, last = list(range(1,10))

print(middle) # [2, 3, 4, 5, 6, 7, 8]


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
"""
值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型，不管解压的电话号码数量是多少(包括0个)。
所以，任何使用到 phone_numbers 变量的代码就不需要做多余的类型检查去确认它是否是列表类型了。
"""

"""
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的。
通常，这些可迭代对象的元素结构有确定的规则（比如第1个元素后面都是电话号码），
星号表达式让开发人员可以很容易的利用这些规则来解压出元素来。
而不是通过一些比较复杂的手段去获取这些关联的的元素值。

值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。
比如，下面是一个带有标签的元组序列：
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
"""
代码示例：
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> homedir
'/var/empty'
>>> sh
'/usr/bin/false'
>>>
"""



# 在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。
# 比如，如果你有一个列表， 你可以很容易的将它分割成前后两部分：

items = [1, 10, 7, 4, 5, 9]
head, *tail = items


# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法。比如：
def sam(nums):
    head, *tail = nums
    return (head + sam(tail)) if tail else head
"""
然后，由于语言层面的限制，递归并不是Python擅长的。
因此，最后那个递归演示仅仅是个好奇的探索罢了，对这个不要太认真了。
"""























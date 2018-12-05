
## pre 前置条件
"""
The for statement in Python operates on iterators.
Objects are iterable (an interface) if they have an __iter__ method that returns an iterator.
"""

## 语法
"""
for <name> in <expression>:
    <suite>
"""


"""
To execute a for statement, Python evaluates the header <expression>,
which must yield an iterable value.
Then, the iter function is applied to that value.
Until a StopIteration exception is raised, Python repeatedly calls next on that iterator
and binds the result to the <name> in the for statement. Then, it executes the <suite>.
"""
counts = [1, 2, 3]
for item in counts:
    print(item)

## 模拟
items = iter(counts)
try:
    while True:
        item = next(items)
        print(item)
except StopIteration:
    pass












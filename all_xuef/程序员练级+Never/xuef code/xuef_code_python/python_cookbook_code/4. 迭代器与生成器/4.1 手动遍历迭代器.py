
"""
问题
你想遍历一个可迭代对象中的所有元素，但是却不想使用for循环。
"""
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

# 讨论
##大多数情况下，我们会使用 for 循环语句用来遍历一个可迭代对象。
##但是，偶尔也需要对迭代做更加精确的控制，这时候了解底层迭代机制就显得尤为重要了。

items = [1, 2, 3]
# Get the iterator
it = iter(items) # Invokes items.__iter__()

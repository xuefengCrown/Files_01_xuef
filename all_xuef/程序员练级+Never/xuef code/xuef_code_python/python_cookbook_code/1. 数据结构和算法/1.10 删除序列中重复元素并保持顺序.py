
"""
关键：
1. 元素保持顺序
2. 元素是否可 hash
    可哈希对象是对象拥有__hash__(self)内置函数的对象。
    对于可哈希的对象执行这个函数将会返回一个整数。
"""



def dedup(items):
    """ 删除序列中重复元素并保持元素原来顺序
        pre:items中的元素可hash """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def test():
    # 整数是可 hash 的
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    b = dedup(a)
    print(list(b))
          
test()


# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

"""
如果你想基于单个字段、属性或者某个更大的数据结构来消除重复元素，
第二种方案同样可以胜任。
"""
# key函数参数模仿了 sorted() , min() 和 max() 等内置函数的相似功能。
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
# 这里的key参数指定了一个函数，将序列元素转换成 hashable 类型。下面是它的用法示例：

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: d['x']))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]





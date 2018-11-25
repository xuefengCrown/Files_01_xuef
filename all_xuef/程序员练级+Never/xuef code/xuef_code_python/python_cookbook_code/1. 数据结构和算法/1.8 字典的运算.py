"""
问题
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

考虑下面的股票名和价格映射字典：
"""
stores = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 找出股价最高的股票
keys = stores.keys()
prices = stores.values()

# 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。
print(list(zip(keys, prices)))

"""
当比较两个元组的时候，值会先进行比较，然后才是键。
这样的话你就能通过一条简单的语句就能很轻松的实现在字典上的求最值和排序操作了。
>> ("bb", 1) > ("aa", 2)
>> True
"""
max_one = max(zip(prices, keys))
min_one = min(zip(prices, keys))

print("max one:", max_one, "& min one:", min_one)

# 可以使用 zip() 和 sorted() 函数来排列字典数据：
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]






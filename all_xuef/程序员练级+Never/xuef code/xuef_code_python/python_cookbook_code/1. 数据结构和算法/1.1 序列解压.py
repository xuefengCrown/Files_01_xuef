

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, mon, day) = data

print("name=", name, year,mon,day, "price=", price)

# 有时候，你可能只想解压一部分，丢弃其他的值。
_, shares, price, _ = data

"""
这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
包括字符串，文件对象，迭代器和生成器。
python中的可迭代对象:
1. 列表、元祖、字典
2. 字符串，文件对象，迭代器和生成器。
"""
s = 'Hello'
a, b, c, d, e = s

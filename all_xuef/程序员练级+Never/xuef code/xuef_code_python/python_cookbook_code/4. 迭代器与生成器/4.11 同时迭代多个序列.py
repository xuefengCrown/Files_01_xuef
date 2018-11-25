
# 你想同时迭代多个序列，每次分别从一个序列中取一个元素。
# zip() 当你想成对处理数据的时候 zip() 函数是很有用的。
# zip() 会创建一个迭代器来作为结果返回。
# 如果这个不是你想要的效果，那么还可以使用 itertools.zip_longest() 函数来代替。
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

p=print
for x,y in zip(xpts, ypts):
    p(x,y)

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
#使用zip()可以让你将它们打包并生成一个字典：
s = dict(zip(headers,values))


"""
你想创建一个实例，但是希望绕过执行 __init__() 方法。

解决方案: 可以通过 __new__() 方法创建一个未初始化的实例。
"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)

data = {'year':2012, 'month':8, 'day':29}

for key, value in data.items():
    setattr(d, key, value)
#使用 setattr() 方法会让你的代码变得更加通用

#d.__dict__.update(data)

print(d.year)

"""
当我们在反序列对象或者实现某个类方法构造函数时需要绕过 __init__() 方法来创建对象。

同样，在你反序列化JSON数据时产生一个如下的字典对象：
data = { 'year': 2012, 'month': 8, 'day': 29 }
如果你想将它转换成一个Date类型实例，可以使用上面的技术。
"""




















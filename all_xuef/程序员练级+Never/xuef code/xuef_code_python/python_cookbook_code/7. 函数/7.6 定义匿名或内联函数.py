

"""
lambda表达式典型的使用场景是排序或数据reduce等
"""

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10)) # 30
print(b(10)) # 30

"""
这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，
而不是定义时就绑定，这跟函数的默认值参数定义是不同的。
"""


"""
在这里列出来的问题是新手很容易犯的错误，有些新手可能会不恰当的使用lambda表达式。
比如，通过在一个循环或列表推导中创建一个lambda表达式列表，并期望函数能在定义时
就记住每次的迭代值。例如：
"""
# funcs 是个 函数列表
funcs = [lambda x: x+n for n in range(5)]
print(funcs)
for f in funcs:
    print(f(0))

# 但是实际效果是运行是n的值为迭代的最后一个值。现在我们用另一种方式修改一下：
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))




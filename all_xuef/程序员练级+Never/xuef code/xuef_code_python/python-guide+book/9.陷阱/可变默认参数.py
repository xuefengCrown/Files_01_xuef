
##看起来，最让Python程序员感到惊奇的是Python对函数定义中可变默认参数的处理。

##您所写的
def append_to(element, to=[]):
    to.append(element)
    return to

##您所期望的
my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)


##而事实是
##[12]
##[12, 42]

"""
当函数被定义时，Python的默认参数就被创建 一次，而不是每次调用函数的时候创建。
这意味着，如果您使用一个可变默认参数并改变了它，您 将会 在未来所有对此函数的调用中改变这个对象。

"""

#good
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

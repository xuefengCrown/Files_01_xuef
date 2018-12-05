

##如果您知道一个列表或者元组的长度，您可以将其解包并为它的元素取名。
##比如， enumerate() 会对list中的每个项提供包含两个元素的元组：

for index, item in enumerate(some_list):
    # 使用index和item做一些工作


##您也能通过这种方式交换变量：
a, b = b, a


##嵌套解包也能工作：

a, (b, c) = 1, (2, 3)


##在Python 3中，扩展解包的新方法在 PEP 3132 有介绍：

a, *rest = [1, 2, 3] # a = 1, rest = [2, 3]

a, *middle, c = [1, 2, 3, 4] # a = 1, middle = [2, 3], c = 4

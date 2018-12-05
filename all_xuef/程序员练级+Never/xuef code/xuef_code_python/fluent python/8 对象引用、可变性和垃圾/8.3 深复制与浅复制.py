
"""
我强烈建议你在 Python Tutor 网站
http://www.pythontutor.com/visualize.html#mode=edit 中查看示例的交互式动画。
"""

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)

#
l1 is l2
#False
l1==l2
#True
l1[1] is l2[1]
#True

"""
然而，构造方法或 [:] 做的是浅复制（即复制了最外层容器，副本中
的元素是源容器中元素的引用）。如果所有元素都是不可变的，那么这
样没有问题，还能节省内存。但是，如果有可变的元素，可能就会导致
意想不到的问题。
"""

# 深复制

import copy
l3=copy.deepcopy(l1)




"""
理解import的原理机制。
具体来说，import modu 语句将 寻找合适的文件，即调用目录下的 modu.py 文件（如果该文件存在）。
如果没有找到这份文件，Python解释器递归地在 "PYTHONPATH" 环境变量中查找该文件，
如果仍没有找到，将抛出ImportError异常。

一旦找到 modu.py，Python解释器将在隔离的作用域内执行这个模块。所有顶层 语句都会被执行，
包括其他的引用。方法与类的定义将会存储到模块的字典中。然后，这个模块的变量、方法和类
通过命名空间暴露给调用方，这是Python中特别有用和强大的核心概念。
"""

import modules.module_test as m

# ['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'p', 'square']
##m.p(dir(m))

##print(m.__package__)
##print(m.__cached__)
##print(m.__doc__)
##print(m.__file__)
##print(m.__loader__)
##print(m.__spec__)


##使用 from modu import func 能精确定位您想导入的方法并将其放到全局命名空间中。

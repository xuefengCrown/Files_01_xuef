
#python 对象模型

"""
1. is-kind-of
基类与子类
__bases__
issubclass

2. is-instance-of
类与实例
__class__, type(a)
isinstanceof

"""

##class A
"""
A 既是class对象(A()创建实例对象)，又是instance对象(A是metaclass对象经过实例化得到的)

"""

##？python2.2之前与之后


##可调用
"""
在 Python中，不只有函数可以被调用，一切对象都有可能可以被调用。
在 Python中，所谓调用，就是执行对象的type所对应的 class对象的 tp_call 操作。
"""

##类型？？？
"""
从2.2开始，Python在启动时，会对类型系统(对象模型)进行初始化的动作。
list对应的PyList_Type 在Python启动后已经作为全局对象存在了，需要的仅仅是完善;
而 A对应的 class对象则不存在，需要申请内存，并创建、初始化。。

"""


##自定义类
"""
class 的元信息是指关于 class的信息，如class name,它所拥有的属性，方法等。
在Python 中，元信息的概念被发挥的淋漓尽致，使得它具有十分灵活的动态性。
"""



















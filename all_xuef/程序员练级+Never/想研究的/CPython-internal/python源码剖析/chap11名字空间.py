

a = 1
b = 2

##def f()对应的 MAKE_FUNCTION 指令代码调用 PyFunction_New之前，globals内容
#print(globals())
print(locals())
def f():
    print("function f")

"""
f调用时，其对应的 PyFrameObject的 f_globals包含这里定义的所有符号，这使得
在函数 f中可以使用 a、b,正是依靠这个 globals的传递，才使得函数 f可以使用函数
f 以外的符号。
"""
def g():
    print("function g")

#f()

##PyFunctionObject
"""
PyFunctionObject 是运行时对象，我们是否可以在 Python代码中侦测？
"""

##f_globals 与 f_locals
## f 中为什么能调用自身(即 python为什么能支持递归?)
"""
STORE_NAME 是将一个符号和符号对应的值存放到当前 PyFrameObject对象的 local名字空间 f_locals中。
当开始执行 func_0.py 时，第一次进入 PyEval_EvalFrameEx时的那个作为参数的PyFrameObject对象，它的
f_locals 和 f_globals 竟然是指向同一个 PyDictObject 的。因为func_0.py外层，什么都没有了。
所以，当 STORE_NAME 指令将符号 f 放入local 名字空间 f_locals 时，也就同时将 f 放进 f_globals中了。


"""
###Python 依靠的是运行时的名字空间!!!


















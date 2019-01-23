
sc = """
def f():
  print("function")
f()
"""
import dis

#dis.dis(sc)
"""
  2           0 LOAD_CONST               0 (<code object f at 0x03564758, file "<dis>", line 2>)
              2 LOAD_CONST               1 ('f')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (f)

  4           8 LOAD_NAME                0 (f)
             10 CALL_FUNCTION            0
             12 POP_TOP
             14 LOAD_CONST               2 (None)
             16 RETURN_VALUE
"""
##
"""
在 MAKE_FUNCTION之前，Python虚拟机会执行 LOAD_CONST 0.
这条指令会将函数 f 对应的 P有CodeObject对象压入到运行时栈中。
所以在执行MAKE_FUNCTION 时，首先就是将这个 PyCodeObject 对象弹出，然后以该对象和
当前 PyFrameObject 对象中维护的 global名字空间 f_globals 对象为参数创建一个新的
PyFunctionObject 对象，而这个 f_globals,将成为函数 f 在运行时的 global名字空间。

"""

def f():
    print("hello world.")

##inspect f对应的 PyCodeObject
code_obj_of_f = f.__code__
print(code_obj_of_f.co_consts)
print(code_obj_of_f.co_name)
print(dir(code_obj_of_f))

##函数调用 CALL_FUNCTION 的参数是干嘛用的？
###当前运行时栈的栈顶指针？为什么需要这个？
"""
def 定义函数时，会将 func_name-->func object 注册进 当前 env
f() 函数调用时，会首先 LOAD_NAME (f)
"""
###函数调用过程
"""
创建新的栈帧，在新的栈帧中执行代码。
"""













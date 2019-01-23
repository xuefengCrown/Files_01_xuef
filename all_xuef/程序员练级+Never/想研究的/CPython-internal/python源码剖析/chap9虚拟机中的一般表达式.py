

##9.1 内建对象的创建
"""
分析对应的 PyCodeObject 对象中的长凉飙 co_consts 和符号表 co_names 入手。

我们的重点放在字节码指令将如何影响当前活动的 PyFrameObject 对象中的运行时栈 和
local 名字空间。(f->f_locals)
字节码之灵对符号或常量的操作最终都将反映到运行时栈和 local名字空间中。
"""

##9.2 复杂内建对象的创建


##9.3 其他表达式
"""
a = 2 #/1
b = a #/2

LOAD_NAME  (a)

在 local 名字空间中查找变量名对应的变量值(f->f_locals)
在 global 名字空间中查找变量名对应的变量值(f->f_globals)
在 builtin 名字空间中查找变量名对应的变量值(f->f_builtins)
"""






















#探索字节码的工具
"""
import dis

byteplay
"""

#source code-->code object
#然后送给解释器执行

#我们可以手动编译代码，使用 compile

print(help(compile))

"""
compile(open("test.py").read(),"test.py", "exec")
  The mode must be 'exec' to compile a module
"""

#.py文件就是一个 module


#关于 Frames, function calls, and scope
"""
Include/code.h
Include/frameobject.h
Objects/frameobject.c
Python/ceval.c
"""


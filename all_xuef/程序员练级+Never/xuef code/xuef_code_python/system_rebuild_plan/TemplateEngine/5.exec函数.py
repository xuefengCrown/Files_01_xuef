# exec函数 https://www.programiz.com/python-programming/methods/built-in/exec

"""
The exec() method executes the dynamically created program, which is either
a string or a code object.
The syntax of exec();
    exec(object, globals, locals)
"""
##exec函数执行一串包含python代码的字符串，它的第二个参数是一个字典，
##用来收集字符串代码中定义的全局变量。举例来说，如果我们这样做：
python_source = """\
SEVENTEEN = 17

def three():
    return 3
"""
#If you pass an empty dictionary as globals, only the __builtins__ are available
# to the object (first parameter to the exec()).
global_namespace = {'__builtins__': None}
exec(python_source, global_namespace)
print(global_namespace)

from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})
# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})

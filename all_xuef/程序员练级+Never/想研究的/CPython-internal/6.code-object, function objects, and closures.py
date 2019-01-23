#Lecture 6 - Code objects, function objects, and closures
"""
·Include/code.h
·Include/funcobject.h
·Objects/codeobject.c
·Objects/funcobject.c
"""

##Learning Objective
"""
To understand how Python functions are simply PyObject structures.
"""


##侦测 function
def f(x,y):
    return x+y
"""
dir(f)
"""
print(dir(f))
print('-'*20)
print(f.__globals__)#为什么每个 function object 需要维护这么一个指向 globals的 指针?

##function 不只是code, 还包含它被定义时的环境(saved-env)


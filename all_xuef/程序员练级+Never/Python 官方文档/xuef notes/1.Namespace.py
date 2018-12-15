
# A namespace is a mapping from names to objects.
# Most namespaces are currently implemented as Python dictionaries.
## 例如
"""
the set of built-in names (containing functions such as abs(), and built-in exception names);
the global names in a module;
and the local names in a function invocation.
In a sense the set of attributes of an object also form a namespace.

"""

# 各个 namespace是隔离的
"""
The important thing to know about namespaces is that
there is absolutely no relation between names in different namespaces;
for instance, two different modules may both define a function maximize without confusion —
users of the modules must prefix it with the module name.

"""

# Attributes may be read-only or writable.
"""
modname.the_answer = 42
del modname.the_answer
"""

# Namespaces are created at different moments and have different lifetimes.
##The namespace containing the built-in names is created when the Python interpreter starts up,
##and is never deleted.

##The global namespace for a module is created when the module definition is read in;
##normally, module namespaces also last until the interpreter quits.

##The local namespace for a function is created when the function is called,
##and deleted when the function returns or raises an exception that is not handled
##within the function.
## Of course, recursive invocations each have their own local namespace.

# If there is a function inside another function, a new scope is nested inside the local scope.

"""
LEGB-rule
在一个Python程序运行中，至少有4个scopes是存在的。
直接访问一个变量可能在这四个namespace中逐一搜索。

Local(innermost)
    包含局部变量。比如一个函数/方法内部。
Enclosing
    包含了非局部(non-local)也非全局(non-global)的变量。
    比如两个嵌套函数，内层函数可能搜索外层函数的namespace，
    但该namespace对内层函数而言既非局部也非全局。 
Global(next-to-last)
    当前脚本的最外层。
    比如当前模块的全局变量。 
Built-in(outtermost)
    Python __builtin__ 模块。包含了内建的变量/关键字等。
"""

# for
##对于大部分语言（比如 C 语言）而言， for-loop 会引入一个新的作用域。
##但Python有点一样却又不太一样。
for i in [1,2]:
    print("inner ",i)
print("outer ",i)


"""
而对于Python 2和Python 3，生成器表达式都有引入新的作用域。

为了让列表推导式和生成器表达式的表现一致，
在Python 3中，列表推导式也有引入一个新的作用域。
"""













def get_func():
    v = "inner"
    def inner_func():
        print(v)
    return inner_func

show_v = get_func()
#show_v()

##与get_func对应的 PyCodeObject对象中的 co_cellvars就应该包含 'v',
##因为其嵌套作用域(inner_func的作用域)中使用了这个符号;
print(get_func.__code__.co_cellvars)
print(show_v.__code__.co_freevars)

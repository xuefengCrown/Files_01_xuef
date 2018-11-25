


class D():
    def __init__(self, func):
        print("初始化")
        print("func name is", func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs): # obj() 时会调用__call()方法
        print(self.__func.__name__, "is called")
        ret = self.__func(*args, **kwargs)
        return ret

@D # ===> add = D(add)
def add(a, b):
    return a + b

# add 指向 D的一个对象
print(add.__dict__)
print(add._D__func(2,2))# 原始的未包装的函数
ret = add(1,1)
print(ret)


p=print

class A:
    @classmethod
    def clsmethod(cls): #@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
        print(cls)

#p(A.__dict__)

A.clsmethod()
p(A)

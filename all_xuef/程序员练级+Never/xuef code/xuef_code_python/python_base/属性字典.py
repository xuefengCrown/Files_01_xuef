

"""

"""

class A():
    cls_pro = 100 # 类属性 A.__dict__

    def __init__(self):
        self.obj_pro = 10 #自定义属性 a.__dict__

    def __getattr__(self, pro_name):
        print("属性访问..")
        return 99

p=print

a=A()

p(A.__dict__)
p('-'*20)
p(a.__dict__)
p('-'*20)
p(a.obj_pro)
p('-'*20)
p(a.non_pro)


"""
with open() as f:
的原理
"""
class File():
    def __init__(self,filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        print("enter..")
        # self.f 扩大f的作用域，以使得__exit__()能关闭 f
        self.f = open(self.filename, self.mode)
        return self.f
    def __exit__(self, *args):
        print("will exit")
        self.f.close()

with File("tmp.txt", "w") as f: # f== __enter__()的返回值
    f.write("hello, xuef")

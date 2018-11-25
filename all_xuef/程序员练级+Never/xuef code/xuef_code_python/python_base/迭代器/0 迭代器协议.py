
# 可迭代对象: 实现了 __iter__方法的对象
# 迭代器: 实现了 __iter__ 和 __next__

#??? 为什么要迭代器
# 迭代器保存了生成数据的方式(一种约定), 而不是保存结果。真正需要时才生成数据

class ClassMates:
    def __init__(self):
        self.members = []
        self.idx = 0
    def add(self, name):
        self.members.append(name)
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < len(self.members):
            ret = self.members[self.idx]
            self.idx += 1
            return ret
        else:
            raise StopIteration      

cm = ClassMates()
for c in 'hello':
    cm.add(c*3)

# 1. 调用cm的__iter__, 返回一个迭代器对象
# 2. 不断调用该迭代器对象的 __next__
for m in cm:
    print(m)


"""
可迭代的 vs 迭代器
"""

class Classmates():
    def __init__(self):
        self.mates = ['aa', 'bb', 'cc']

    def __iter__(self):
        return C_Iterator(self.mates)


class C_Iterator():
    def __init__(self, items):
        self.items = items
        self.idx = 0

    def __iter__(self):
        return self
    def __next__(self):
        try:
            item = self.items[self.idx]
            self.idx += 1
        except:
            raise StopIteration
        return item
    
c = Classmates()
for i in c:
    print(i)

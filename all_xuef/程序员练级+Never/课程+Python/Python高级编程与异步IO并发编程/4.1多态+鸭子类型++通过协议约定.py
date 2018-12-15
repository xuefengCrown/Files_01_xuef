
"""
java中的多态需要语法和语义的强制规定。
而在python中，只需要也具有某种行为(定义了某方法)

"""

class Cat:
    def say(self):
        print("I am a cat...")


class Dog:
    def say(self):
        print("I am a dog...")

class Duck:
    def say(self):
        print("I am a duck...")


animals = [Cat, Dog, Duck]
for a in animals:
    a().say()

    
#理解python的动态性。它不会强制什么，它喜欢协议和口头约定。

## 这使得代码可以非常简洁
"""
Python中的迭代器协议，将 list, dict, set, 文件等一大批实现了迭代器协议的对象被提升为
Iterable对象。于是可以实现更加通用的操作，代码可以很简洁！！！
这来自于准确的抽象！！！

"""









    

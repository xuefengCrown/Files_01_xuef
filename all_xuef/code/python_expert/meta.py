#coding:utf-8

# library.py
class Base:
    def foo(self):
        return "Base foo()"

assert hasattr(Base, 'foo'), "you broke it, you fool!"
# user.py
class Derived(Base):
    def bar(self):
        return self.foo()

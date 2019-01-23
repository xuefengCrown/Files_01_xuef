
"""
你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，
比如类型检查或合法性验证。
"""

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Guido')
a.first_name = 11 # Calls the setter







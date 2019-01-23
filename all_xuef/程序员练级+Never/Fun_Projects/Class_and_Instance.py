
"""
To implement an object system in full, we send messages between instances, classes,
and base classes, all of which are dictionaries that contain attributes.
"""
#comments by xuef
##注意到对象其实不必依赖于类而存在，我们可以直接创建一个对象!在JavaScript中允许这么做。
##对象是什么？对象其实就是一个值，只不过我们可以向它发送消息并获得响应。
##注意<class 'function'>与<class 'method'>(bound methods)的区别，以及我们这里是如何
##将instance绑定到self的。
##实现对象系统有两个工作: 提供语法上的支持，提供语义上的支持。前者涉及词法语法分析，后者方便的多。

def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionay."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
        
    attributes = {}
    #The instance is a dispatch dictionary that responds to the messages get and set.
    instance = {'get': get_value, 'set': set_value, 'dict': attributes}
    return instance

def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        def method(*args):
            #将instance绑定到self,注意这里不支持 static method!
            return value(instance, *args)
        return method
    else:
        return value


#A class is also an object, both in Python's object system
#and the system we are implementing here. 
def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary."""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    def new(*args):
        return init_instance(cls, *args)
    
    #A class can respond to get and set messages, as well as the new message
    cls = {'get': get_value, 'set': set_value, 'new': new, 'dict': attributes}
    return cls

def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


#Test
def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    interest = 0.02
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')
    return make_class(locals())

Acc = make_account_class()
#print(Acc['dict'])
acc1 = Acc['new']('xuef')
print(acc1['get']('deposit')) #bind_method
print(acc1['dict'])












    

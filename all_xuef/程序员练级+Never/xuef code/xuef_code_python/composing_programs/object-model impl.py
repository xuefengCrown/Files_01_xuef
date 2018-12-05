
"""
To implement an object system in full, we send messages between instances, classes,
and base classes, all of which are dictionaries that contain attributes.

We will not implement the entire Python object system, which includes features that
we have not covered in this text (e.g., meta-classes and static methods).

We will focus instead on user-defined classes without multiple inheritance and
without introspective(内省的) behavior (such as returning the class of an instance).
Our implementation is not meant to follow the precise specification of the Python type system.
Instead, it is designed to implement the core functionality that enables the object metaphor.
"""
import pdb
#The instance is a dispatch dictionary that responds to the messages get and set.
def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    def get_value(name):
##        if name does not appear in the local attributes dictionary,
##        then it is looked up in the class. If the value returned by cls is a function,
##        it must be bound to the instance.
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):
        # bound the value (a func returned by cls) to the instance
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value

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
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


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
    """
        {'withdraw': <function make_account_class.<locals>.withdraw at 0x04521108>,
        'deposit': <function make_account_class.<locals>.deposit at 0x045210C0>,
        '__init__': <function make_account_class.<locals>.__init__ at 0x04521078>,
        'interest': 0.02}
    """
    return make_class(locals())
pdb.set_trace()
Account = make_account_class()
kirk_account = Account['new']('Kirk')



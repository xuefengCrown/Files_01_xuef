#coding:utf-8

def mult_closure(x):
    def wrapped(y):
        # wrapped closes over the 'x' variable
        return x * y
    
    return wrapped

mult_by_three = mult_closure(3)

"""
when 2 use a closure?
1. Great to dry up code. add syntatic suger.
2. you need to write a complicated generator.
3. monkey patch a function you can't change.
4. dynamically build behavior by 'stacking' functions.
"""
# monkey patch example
def bad_func_from_library(some_attr):
    some_attr / 0

def dont_panic_closure(bad_func):
    def wrapped(some_attr):
        try:
            # 总是持有对 bad_func 的引用，即使 return wrapped 后
            bad_func(some_attr) # wrapped closes over bad_func
        except:
            print("The bad function ...")

    return wrapped















            
































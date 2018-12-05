
"""
We can use higher-order functions to convert a function that takes multiple arguments
into a chain of functions that each take a single argument.

More specifically, given a function f(x, y), we can define a function g such that g(x)(y)
is equivalent to f(x, y).

Here, g is a higher-order function that takes in a single argument x and
returns another function that takes in a single argument y.
This transformation is called currying.

"""

def curried_pow(x):
    def g(y):
        return x**y
    return g

p=print
p(curried_pow(2)(3))
##In more general languages such as Python, currying is useful when we require a function
##that takes in only a single argument. For example, the map pattern applies a single-argument
##function to a sequence of values.

# currying
def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f


    

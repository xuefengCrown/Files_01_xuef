
"""
Python also allows us to define objects that can be "called" like functions by including
a __call__ method. With this method, we can define a class that behaves like a higher-order
function.
"""

def make_adder(n):
    def adder(k):
        return n + k
    return adder
add_three = make_adder(3)
add_three(4)


# We can create an Adder class that defines a __call__ method to provide the same functionality.
class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k
add_three_obj = Adder(3)
add_three_obj(4)

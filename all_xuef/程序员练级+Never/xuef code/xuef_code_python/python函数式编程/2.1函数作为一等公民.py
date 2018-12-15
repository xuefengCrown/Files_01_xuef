"""
We'll look at each of the following functional programming topics:
•  First-class and higher-order functions, which are also known as pure functions.
•  Immutable Data.
•  Strict and non-strict evaluation. We can also call this eager vs. lazy evaluation.
•  Recursion instead of an explicit loop state.
•  Functional type systems.


Functional programming is often succinct and expressive. One way to achieve
this is by providing functions as arguments and return values for other functions.
"""
#To write a pure function in Python, we have to write local-only code. 
import dis

def f(a):
    def f2():
        nonlocal a
        a = 2
    return f2

print(dis.dis(f))

#Because lambda's can't have assignment statements, they're always pure functions
#and suitable for functional programming.



#car, cdr













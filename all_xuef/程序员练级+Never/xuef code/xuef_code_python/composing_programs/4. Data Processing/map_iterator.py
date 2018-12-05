"""
The map function is lazy: calling it does not perform the computation required to
compute elements of its result. Instead, an iterator object is created that can return
results if queried using next.
"""

def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x
s = range(3, 7)
doubled = map(double_and_print, s)  # double_and_print not yet called
next(doubled)                       # double_and_print called once
##*** 3 => 6 ***
##6

"""
The filter function returns an iterator over a subset of the values in another iterable.
The zip function returns an iterator over tuples of values that combine one value from
each of multiple iterables.
"""

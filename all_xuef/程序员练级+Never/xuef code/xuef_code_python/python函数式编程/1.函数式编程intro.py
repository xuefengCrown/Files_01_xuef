

"""
We can't easily create purely functional programs in Python.
Python lacks a number of features that would be required for this.
For example, we don't have unlimited recursion, lazy evaluation of all expressions,
and an optimizing compiler.
"""
# Generally, Python emphasizes strict evaluation rules.
##This means that statements are executed in order and expressions are evaluated from left to right.
##While this deviates(偏离) from functional purity,
##it allows us to perform manual optimizations when writing in Python. 

"""
One of the most important is the idea that functions are
first-class objects. In some languages, functions exist only as a source code
construct: they don't exist as proper data structures at runtime. In Python,
functions can use functions as arguments and return functions as results.
"""

"""
Functional programs often exploit(利用) immutable data structures. The emphasis on
stateless objects permits flexible optimization. Python offers tuples and namedtuples
as complex but immutable objects. We can leverage these structures to adapt some
design practices from other functional programming languages.
"""

"""
Many functional languages emphasize recursion but exploit Tail-Call Optimization
(TCO). Python tends to limit recursion to a relatively small number of stack frames.
In many cases, we can think of a recursion as a generator function. We can then simply
rewrite it to use a  yield from statement, doing the tail-call optimization ourselves.

We'll look at the core features of functional programming from a Python point of view.
Our objective is to borrow good ideas from functional programming languages, and
use these ideas to create expressive and succinct applications in Python.
"""
















## If we are to build larger systems
"""
1. We will need a good way to separate the system into relatively self-contained parts,
and to document the dependencies between those parts.

2. We will need a better way to control the scope and binding of names.
Lexical scoping is a powerful tool for name control, but it is not sufficient
when programs may be large or split up over multiple sources.

3. We will need a way to enforce abstraction boundaries.
In chap2, we introduced the idea of an abstract data type. Inside the implementation of the type,
we can manipulate the values arbitrarily, but outside the implementation,
the values of the type are to be created and manipulated only by the procedures
in the interface of that type. We call this an abstraction boundary.
If a program respects this boundary, we can change the implementation of the data type.
If, however, some piece of code breaks the abstraction by relying on the details
of the implementation, then we can no longer change the implementation
freely without breaking other code.

4. Last, we need a way to combine  these parts flexibly, so that a single part
may be reused in different contexts.
"""

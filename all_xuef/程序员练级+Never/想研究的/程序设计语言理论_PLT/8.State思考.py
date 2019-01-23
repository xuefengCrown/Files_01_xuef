

"""
State provides a form of modularity. As our very interpreter demonstrates,
without explicit stateful operations, to achieve the same effect:

1.We would need to add explicit parameters and return values that pass the equivalent
of the store around.

2.These changes would have to be made to all procedures that may be involved in a
communication path between producers and consumers of state.

Thus, a different way to think of state in a programming language is that it is an
implicit parameter already passed to and returned from all procedures, without imposing
that burden on the programmer. This enables procedures to communicate “at a distance”
without all the intermediaries having to be aware of the communication.


State makes it possible to construct dynamic, cyclic data structures, or at least
to do so in a relatively straightforward manner.

State gives procedures memory

"""

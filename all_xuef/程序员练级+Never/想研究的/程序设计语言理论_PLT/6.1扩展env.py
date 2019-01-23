
#8.1.6 Introducing the Store
"""
The preceding discussion tells us that we need two repositories to accompany
the expression, not one.
One of them, the environment, continues to be responsible for maintaining lexical scope.
But the environment cannot directly map identifiers to their value,
because the value might change. Instead, something else needs to be
responsible for maintaining the dynamic state of mutated boxes.
This latter data structure is called the store.
"""

##Thus the environment maps names to locations,
##and the store maps locations to values


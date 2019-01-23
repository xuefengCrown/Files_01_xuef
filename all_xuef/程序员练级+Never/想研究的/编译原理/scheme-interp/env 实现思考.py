
##environments的准确语义应该是怎样的？
"""
In effect, saving the environment pointer records which names refer to which pieces of storage.
If other code then executes in that same environment and changes those values,
the new values will be seen by this procedure when it returns and restores the environment pointer.
This policy has two important consequences:
1. we can save an environment pointer into a continuation very quickly, and restore it quickly,
because we're just saving and restoring one pointer, and

2. it ensures that environments have the right semantics: closures that live in the same
environment should see each others' changes to variables. This is one of the ways that
procedures are supposed to be able to communicate--by operating on variables that they can see.
"""

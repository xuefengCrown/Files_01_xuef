
##Types and Type Systems
"""
• A type is a set of values together with a set of operations on those values.

• E.g., fields and methods of a Java class are meant to correspond to values and operations.

• A language’s type system specifies which operations are valid for which types.

• Goal of type checking is to ensure that operations are used with the
correct types, enforcing intended interpretation of values.
"""

##Uses of Types
"""
Help compilation:
– When the Python compiler sees x+y , the static part of its type
systems tells it almost nothing about types of x and y , so code
must be general.
– But during execution, the dynamic part of its type system, imple-
mented by type information in the data structures, tells it what
code to execute.
– In C, C++, Java, code sequences for x+y are smaller and faster,
because representations are known without runtime checks of
type information.

"""

##dynamic type
"""
Use duck typing: define types of things by what operations they respond to.
"""

##Static typing proponents say:
"""
– Static checking catches many programming errors at compile time.
– Avoids overhead of runtime type checks.
– Use various devices to recover the flexibility lost by “going static:”
subtyping, coercions, and type parameterization.
– Of course, each such wrinkle introduces its own complications.
"""


##Using Subtypes???
"""
• In languages such as Java, can define types (classes) either to
– Implement a type, or
– Define the operations on a family of types without (completely) implementing them.
• Hence, relaxes static typing a bit: we may know that something is a
Y without knowing precisely which subtype it has.
"""



















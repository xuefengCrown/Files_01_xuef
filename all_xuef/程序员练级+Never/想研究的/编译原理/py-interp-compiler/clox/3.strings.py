
##
"""
We need a way to support values whose size varies, sometimes greatly.
This is exactly what dynamic allocation on the heap is designed for.
We can allocate as many bytes as we need.
We get back a pointer that we’ll use to keep track of the value as
it flows through the VM.
"""

##Values and Objects
"""
Every Lox value that you can store in a variable or return from an expression will be a Value.
For small fixed-size types like numbers, the payload is stored directly inside the Value struct
itself.

If the object is larger, its data lives on the heap. Then the Value’s payload is a pointer
to that blob of memory. We’ll eventually have a handful of heap-allocated types in clox:
strings, instances, functions, you get the idea.

"""

##Struct Inheritance


##Operations on string
"""
Full-grown languages provide lots of operations for working with strings—
access to individual characters, the string’s length, changing case, splitting,
joining, searching, etc.
"""
### +
"""
Since Lox is dynamically typed, we can’t tell which behavior is needed at
compile time because we don’t know the types of the operands until runtime.
Thus, the OP_ADD instruction dynamically inspects the operands and chooses
the right operation.

"""

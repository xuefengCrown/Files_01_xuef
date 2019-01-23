
"""
Languags where variables can be given (nontrivial) types are called typed languages.

Languages that do not restrict the range of variables are called untyped languages:
they do not have types
or, equivalently, have a single universal type that contains all values. 

In these languages, operations may be applied to inappropriate arguments:
the result may be
a fixed arbitrary value, a fault, an exception, or an unspecified effect.

The pure λ-calculus is an extreme case of an untyped language
where no fault ever occurs: the only operation is function application
and, since all values are functions, that operation never fails.


A type system is that component of a typed language that keeps track of the types of
variables and, in general, of the types of all expressions in a program. 

Type systems are used to determine whether programs are well behaved.


"""
# Comments on Haskell
"""
Haskell has a static type system.
The type of every expression is known at compile time, which leads to safer code.

Everything in Haskell has a type, so the compiler can reason quite a lot about
your program before compiling it.

Unlike Java or Pascal, Haskell has type inference.
If we write a number, we don't have to tell Haskell it's a number.
It can infer that on its own, so we don't have to explicitly write out the types of
our functions and expressions to get things done.

However, understanding the type system is a very important part of learning Haskell.

A type is a kind of label that every expression has. It tells us in which category of
things that expression fits.
The expression True is a boolean, "hello" is a string, etc.

Functions also have types.
"""
##Typeclasses
"""
You can think of them kind of as Java interfaces, only better.

"""











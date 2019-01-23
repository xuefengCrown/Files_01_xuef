
#从类型的角度来看运算

##扩展 比较操作 到其他类型
"""
Allowing comparisons on types other than numbers could be useful.
在 Python中，字符串类型和tuple类型是允许比较操作的

Would you extend Lox to support comparing other types? If so, which pairs of types
do you allow and how do you define their ordering? Justify your choices and compare
them to other languages.

"""

##Even comparisons among mixed types?
##是否有意义 比如 2 < "hello"
##operator among mix types  有时是有意义的！
"""
在 Python中， 'hello'*3 --> 'hellohellohello'

有些语言支持 "scone" + 4 --> scone4
"""


## /0 问题
"""
What happens right now if you divide a number by zero? What do you think should happen?
Justify your choice. How do other languages you know handle division by zero and why do
they make the choices they do?

Change the implementation in visitBinaryExpr() to detect and report a runtime error for
this case.
"""

##STATIC AND DYNAMIC TYPING
"""
Some languages, like Java, are statically typed which means type errors are detected and
reported at compile time before any code is run.

Others, like Lox, are dynamically typed and defer checking for type errors until runtime
right before an operation is attempted. We tend to consider this a black-and-white choice,
but there is actually a continuum between them.

It turns out even most statically typed languages do some type checks at runtime.
The type system checks most type rules statically, but inserts runtime checks in
the generated code for other operations.

For example, in Java, the static type system assumes a cast expression will always
safely succeed. After you cast some value, you can statically treat it as the destination type
and not get any compile errors.

But downcasts can fail, obviously. The only reason the static checker can presume that
casts always succeed without violating the language’s soundness guarantees is because
the cast is checked at runtime and throws an exception on failure.

A more subtle example is covariant arrays in Java and C#. The static subtyping rules
for arrays allow operations that are not sound. Consider:

Object[] stuff = new Integer[1];
stuff[0] = "not an int!";
This code compiles without any errors. The first line upcasts the Integer array and stores
it in a variable of type Object array. The second line stores a string in one of its cells.
The Object array type statically allows that—strings are Objects—but the actual Integer array
that stuff refers to at runtime should never have a string in it!

To avoid that catastrophe, when you store a value in an array, the JVM does a runtime check
to make sure it’s an allowed type. If not, it throws an ArrayStoreException.


There are few modern statically typed languages that don’t do any of their type validation
at runtime. If you find yourself designing a statically typed language, keep in mind that
you can sometimes give users more flexibility without sacrificing too many of the benefits
of static safety by deferring some type checks until runtime.

On the other hand, a key reason users choose statically typed languages is because of the
confidence the language gives them that certain kinds of errors can never occur when their
program is run.

"""






















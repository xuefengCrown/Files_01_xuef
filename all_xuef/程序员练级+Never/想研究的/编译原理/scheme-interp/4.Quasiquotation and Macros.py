#Quasiquotation and Macros
"""
Quasiquotation allows you to specify patterns that can be used to construct data structures,
and also specify how to fill in "holes" in the patterns. In effect, you can define a template
for a data structure, much like a quoted data structure, but also specify how to fill in holes
to create variations on the data structure.

With macros, you can write "templates" for programs, which you can customize by filling in
the holes. This lets you create both code-structuring and data-structuring facilities that
express stereotyped patterns with variations.
"""
##
"""
[ Scheme macros are actually more powerful than this, however, because you can use them to
analyze code before transforming it... sort of... ]
"""

##`
"""
quasiquote constructs an s-expression at run time,
when the quasiquote form is executed. This allows Scheme to "customize" a data structure,
so that you actually get a different data structure each time you execute the same quasiquote form.

Scheme>(define bar 2)
baz
Scheme>(quasiquote (foo (unquote bar) baz))
(foo 2 baz)


(define (create-shipping-employee-association name)
  `((name ,name)
    (employee-id-no ,(get-next-employee-id!))
    (department shipping)
    (hire-date ,(get-day) ,(get-month) ,(get-year))))
"""

##,@

##macro
"""
By writing a macro, what you're really doing is extending the functionality of the compiler
or interpreter--you're telling it how to compile (or interpret) a new construct,
by telling it how to rewrite that construct into something it already knows
how to compile or interpret.
"""


##Macros vs. Procedures
"""
Why do we want macros? In Scheme, the main code abstraction mechanism is
procedural abstraction-- using define or lambda to write procedures that
do stereotyped(模式化的) things.

In a sense, we "specialize" procedures by passing them argument values--a procedure can do
different things depending on the values it's given to work with.
We can also "specialize" procedures by creating closures in different environments.
Isn't this enough?


Notice that you can't write or as a procedure. If or were a procedure, both of its arguments
would always be evaluated before the actual procedure call. Since or is only supposed to
evaluate its second argument if the first one returns #f, it just wouldn't work.

"""

##Automating the Construction of Abstract Data Types with Macros
"""
As I just showed, it's easy to define an abstract data type in Scheme, by hand,
using procedural abstraction. Doing this for every abstract data type is very tedious,
however, so it would be good to automate the process and provide a
declarative interface to it.
"""



























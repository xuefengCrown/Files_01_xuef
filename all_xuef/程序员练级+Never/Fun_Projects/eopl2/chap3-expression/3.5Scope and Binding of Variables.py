
#3.5 Scoping and Binding of Variables
"""
In most programming languages, variables may appear in two different ways:
as references or as declarations.
A variable reference is a use of the variable.
"""
##declaration
"""
(lambda (x) (+ x 3))
or
(let ((x (+ y 7))) (+ x 3))
the first occurrence of x is a declaration: it introduces the variable as a name
for some value.
"""
##Declarations in most programming languages have a limited scope

##scoping rules
"""
Every programming language must have some rules to determine the declaration
to which each variable reference refers.
These rules are typically called scoping rules.
"""
## lexical scoping
"""
We can determine which declaration is associated with each variable use
without executing the program.
Properties like this, which can be computed without executing the program,
are called static properties.

To find which declaration corresponds to a given use of a variable, we
search outward from the use until we find a declaration of the variable.
"""
####A variable declared by a proc is bound when the procedure is applied.
####A let-variable is bound by the value of its right-hand side.














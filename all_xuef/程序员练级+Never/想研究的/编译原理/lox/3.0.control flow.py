
#control flow
"""
We can divide control flow roughly into two kinds:
1.Conditional or branching control flow is used to not execute some piece of code.
2.Looping control flow executes a chunk of code more than once. It jumps back so that
you can do something again. Since you don’t usually want infinite loops, it typically
has some conditional logic to know when to stop looping as well.
"""
##添加 if statement
###syntax
"""
statement → exprStmt
          | ifStmt
          | printStmt
          | block ;

ifStmt    → "if" "(" expression ")" statement ( "else" statement )? ;
"""

##nesting if
"""
Instead, most languages and parsers avoid the problem in an ad hoc way.
No matter what hack they use to get themselves out of the trouble, they always
choose the same interpretation—the else is bound to the nearest if that precedes it.
"""

##Logical Operators

###the logical operators and (&&) and or (||).
"""
These aren’t like other binary operators because they short-circuit.
"""
####syntax
"""
expression → assignment ;
assignment → identifier "=" assignment
           | logic_or ;
logic_or   → logic_and ( "or" logic_and )* ;
logic_and  → equality ( "and" equality )* ;

As in C, they each have their own precedence with || lower than &&.
"""

##While Loops
"""
statement → exprStmt
          | ifStmt
          | printStmt
          | whileStmt
          | block ;

whileStmt → "while" "(" expression ")" statement ;
"""

##For Loops
"""
Most modern languages have a higher-level looping statement for iterating over
arbitrary user-defined sequences.

iteration protocol that the for loop could use.

statement → exprStmt
          | forStmt
          | ifStmt
          | printStmt
          | whileStmt
          | block ;

forStmt   → "for" "(" ( varDecl | exprStmt | ";" )
                      expression? ";"
                      expression? ")" statement ;
"""
#for (var i = 0; i < 10; i = i + 1) print i;
##值得注意的是， i 的作用域!?

###desugaring
"""
for form --> while form

Instead of directly interpreting for loops, the parser will consume the new syntax and
translate it to more primitive forms that the interpreter already knows how to execute.

desugaring is a powerful tool to have in your toolbox and this gives me an excuse to
show it to you. In a sophisticated implementation, the backend does lots of work
optimizing each supported chunk of semantics.
The fewer of those there are, the more mileage it gets out of each optimization.

"""



































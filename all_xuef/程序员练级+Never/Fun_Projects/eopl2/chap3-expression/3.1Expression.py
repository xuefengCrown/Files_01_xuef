
#front-end
"""
No matter what implementation strategy we use, we need a front end
that converts programs into abstract syntax trees.

Because programs are just strings of characters, our front end needs to
group these characters into meaningful units.
This grouping is usually divided into two stages: scanning and parsing.

Parsing is the process of organizing the sequence of tokens into
hierarchical syntactic structures such as expressions, statements, and blocks.
This is like organizing (diagramming) a sentence into clauses.
"""

#3.2.1 Specifying the Syntax
"""
(scan&parse "-(55, -(x,11))")
#(struct:a-program
    #(struct:diff-exp
        #(struct:const-exp 55)
        #(struct:diff-exp
            #(struct:var-exp x)
            #(struct:const-exp 11))))
"""
#3.2.2 Specification of Values
"""
An important part of the specification of any programming language is the
set of values that the language manipulates.

Each language has at least two such sets: the expressed values and the denoted values.
The expressed values are the possible values of expressions,
and the denoted values are the values bound to variables.
"""
#3.2.4 Specifying the Behavior of Expressions
"""
constructors:
    const-exp : Int → Exp
    zero?-exp : Exp → Exp
    if-exp : Exp × Exp × Exp → Exp
    diff-exp : Exp × Exp → Exp
    var-exp : Var → Exp
    let-exp : Var × Exp × Exp → Exp

observer:
    value-of : Exp × Env → ExpVal

Before starting on an implementation, we write down a specification for
the behavior of these procedures. Following the interpreter recipe, we expect
that value-of will look at the expression, determine what kind of expression
it is, and return the appropriate value.
"""



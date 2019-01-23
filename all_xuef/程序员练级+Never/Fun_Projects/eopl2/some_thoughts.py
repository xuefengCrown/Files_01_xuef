
#3 Environment-Passing Interpreters
"""
The syntax tree is then passed to the interpreter, which is a program
that looks at a data structure and performs some actions that depend on its structure.
In the case of a language-processing system, the interpreter takes the abstract syntax tree
and converts it, possibly using external inputs, to an answer.
"""
##Each interpreter is a data-driven procedure.
"""
Each of these procedures takes data and performs some action determined by the form of the data.
"""

##
"""
We build this interpreter in stages, starting with the simplest forms:
literals, variables, and primitive applications.
Then we add other forms one at a time.
"""

##the expressed values and the denoted values.
"""
An important part of the specification of any programming language is the set of values that
the language manipulates. Each language has at least two such sets:
the expressed values and the denoted values.
The expressed values are the possible values of expressions,
and the denoted values are the values bound to variables.
"""
#### In Scheme,
"""
there are many kinds of expressed values, such as numbers, pairs, characters, and strings,
but there is only one kind of denoted value: locations containing expressed values.
"""

##front-end
"""
Before we can conveniently test our interpreter, however, we need a front end that converts
programs into abstract syntax trees. Because programs are just strings of characters, our front end
needs to group these characters into meaningful units. This grouping is usually divided into two
stages: scanning and parsing.

The scanner takes a sequence of characters and produces a sequence of tokens.

Parsing is the process of organizing the sequence of tokens into hierarchical syntactic structures
such as expressions, statements, and blocks. This is like organizing (diagramming) a sentence into
clauses.
The parser takes a sequence of tokens from the scanner and produces an abstract syntax tree.
"""
##Another approach is to ignore the details of the concrete syntax
##and to write our expressions as list structures.


##how it helps us
"""
This illustrates how we are dependent on our understanding of the defining language:
if we do not know what Scheme's if does, this code would not help us understand the new
language. In this case, of course, we do understand Scheme's if, and our code provides some
additional information on the defined language's conditional expression as it considers any
nonzero value to be true.
"""

##let
"""
The entire let form is an expression, as is its body, so let expressions may be nested.

let x = 1
in let x = + (x,2)
   in add1(x)
"""

##procedures
"""
So far our language has only the primitive operations that were included in the original language.
For our interpreted language to be at all useful, we must allow new procedures to be created.
"""

##We wish procedures to be first-class values in our language.
##to determine what information must be included in a value representing a procedure.
##To do this, we consider what happens at procedure-application time.
"""
When a procedure is applied, its body is evaluated in an environment that binds the formal
parameters of the procedure to the arguments of the application. Variables occurring free in the
procedure should also obey the lexical binding rule. This requires that they retain the bindings
that were in force at the time the procedure was created.
"""








"""
When writing code for a procedure, we must know precisely
what kinds of values may occur as arguments to the procedure,
and what kinds of values it is legal for the procedure to return.
"""

#归纳法定义数据集合
## def list-of-numbers
"""
Definition 1.1.2 The set list-of-numbers is the smallest set of values
satisfying the two properties:
1. The empty list is a list-of-numbers, and
2. If l is a list-of-numbers and n is a number, then the pair (n . l) is a list-of-numbers.

"""

#BNF notation

"""
BNF was originally developed to specify the syntactic structure of programming languages.

This set of rules is called a grammar.

##终结符，非终结符，Productions
he symbol ::=, read is or can be.

<list-of-numbers>⇒ (<number> . <list-of-numbers>)⇒ (14 . <list-of-numbers>)⇒ (14 . ())
The order in which nonterminals are replaced does not matter.

btree ::= () | (Int btree btree)

Binary-search-tree :: = () | (Int Binary-search-tree Binary-search-tree)

S-list :: = ( { S-exp }∗ )
S-exp :: = Symbol | S-list
"""

##lambda calculus
"""
A simple mini-language that is often used to study the theory of programming languages is the
lambda calculus. This language consists only of variable references, lambda expressions with a
single formal parameter, and procedure calls. We can define it with the following grammar:

<expression> ::= <identifier>
             ::= (lambda (<identifier>) <expression>)
             ::= (<expression> <expression>)

where <identifier> is any symbol other than lambda. This grammar defines the elements of
<expression> as Scheme values, so it is convenient to write programs that manipulate them.
"""

#Induction
"""
Having described sets inductively, we can use the inductive definitions in two ways:
to prove theorems about members of the set and
to write programs that manipulate them.
"""

#the scoping and binding of variables
"""
In most programming languages, variables may appear in two different ways:
as references or as declarations.

(f x y) ## 引用
(lambda (x) (* x x))
"""

##Binding Rule,(for lambda calculus)
####free and bound variable
"""
(lambda (y)
    ((lambda (x) x) y))
"""
######Lambda calculus expressions without free variables are called combinators. 


##occurs-free?(先得occur,然后载free)
"""
Definition 1.3.3 (Occurs Free, Occurs Bound in Lambda Calculus Expressions)
A variable x occurs free in a lambda calculus expression E if and only if
1. E is a variable reference and E is the same as x; or
2. E is of the form (lambda (y) E'), where y is different from x and x occurs free in E'; or
3. E is of the form (E 1 E 2 ) and x occurs free in E 1 or E 2 .

> (occurs-free? ’x ’x)
#t
> (occurs-free? ’x ’y)
#f
> (occurs-free? ’x ’(lambda (x) (x y)))
#f
> (occurs-free? ’x ’(lambda (y) (x y)))
#t
> (occurs-free? ’x ’((lambda (x) x) (x y)))
#t
> (occurs-free? ’x ’(lambda (y) (lambda (z) (x (y z)))))
#t


We can solve this problem by following the grammar for lambda-calculus expressions
LcExp :: = Identifier
      :: = (lambda (Identifier) LcExp)
      :: = (LcExp LcExp)

We can summarize these cases in the rules:
• If the expression e is a variable, then the variable x occurs free in e if
and only if x is the same as e.
• If the expression e is of the form (lambda (y) e ? ), then the variable x
occurs free in e if and only if y is differentfrom x and x occurs free in e? .
• If the expression e is of the form (e 1 e 2 ), then x occurs free in e if
and only if it occurs free in e 1 or e 2 . Here, we use “or” to mean
inclusive or, meaning that this includes the possibility that x occurs
free in both e 1 and e 2 . We will generally use “or” in this sense.

"""

#Execution of the scoping algorithm may then be viewed as a journey
#outward from a variable reference. 
"""
(lambda (x y)
  ((lambda (a)
     (x (a y)))
   x))

"""












   













































#It all depends how deep you want to go, and how much you already know.
#lambda calculus

## procedure application
"""
(+ (* 5 6) (* 8 3))
1. 如何规约
2. when there're several redexes, we have a choice of which one to reduce first.
"""

## 多参数-->单参数 (currying)

## 2.1.3 built-in functions and constants
"""
arithmetic functions(+,-,*,/)
constants(0,1, ...)
logical functions(and, or, not)
constants(TRUE, FALSE)
character('a','b', ...)
if
data constructor(cons),以及配套的 car,cdr(head,tail)
    use cons to build a compound object which can be taken apart with head and tail
    head (cons a b) --> a
    tail (cons a b) --> b

"""

#lambda abstraction
"""
(λx . + x 1)

"""

#the abstract syntax of lambda expressions(in BNF)


#2.2.1 Bound and Free Variables
"""
(λx . + x y) 4
in order to eval this exp completely, we need to know the 'global' value of y

+ x ((λx . + x y) 4)
"""

#Figure2.2 definitions of bound and free
## EOPL中说的也很详细

#2.2.2 Beta-conversion
## how to apply it
"""
function can be argument too

(λf . f 3) (λx . + x 1) --> (λx . + x 1) 3
"""

#Naming
"""
Given a lambda abstraction (λx . E),how can we identify those occurrences
of x which should be substituted for?
It's easy: we should substitute for those occurrences of x which are free in E.
"""

#2.3 Reduction Order


#3 let
"""
a let-exp is an exp like any other, and can be used in the same way as
any other expression.
    + 1 (let x=3 in (* x x))
--> + 1 9
for the same reason, let-exp can be nested.

"""






























































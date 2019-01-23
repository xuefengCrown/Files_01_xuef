
#chap3
"""
3.9 Add list processing operations to the language,
    including cons, car, cdr, null? and emptylist.

3.11

3.12 添加 cond

3.13 这有点像 C语言的行为
 Change the values of the language so that integers are the only expressed values.
Modify if so that the value 0 is treated as false and all other values
are treated as true. Modify the predicates accordingly.

3.16 多绑定的 let

3.17 let*

Exercise 3.32 [**] Extend the language above to allow the declaration of any number
of mututally recursive unary procedures, for example:
letrec
    even(x) = if zero?(x) then 1 else (odd -(x,1))
    odd(x) = if zero?(x) then 0 else (even -(x,1))
in (odd 13)

#(struct:a-program
  #(struct:letrec-exp
    (even odd)
    (x x)
    (#(struct:if-exp
       #(struct:zero?-exp
         #(struct:var-exp x))
       #(struct:const-exp 1)
       #(struct:call-exp
         #(struct:var-exp odd)
         #(struct:diff-exp
           #(struct:var-exp x)
           #(struct:const-exp 1))))
     #(struct:if-exp
       #(struct:zero?-exp
         #(struct:var-exp x))
       #(struct:const-exp 0)
       #(struct:call-exp
         #(struct:var-exp even)
         #(struct:diff-exp
           #(struct:var-exp x)
           #(struct:const-exp 1)))))
    #(struct:call-exp
      #(struct:var-exp odd)
      #(struct:const-exp 13))))

Exercise 3.33 [**] Extend the language above to allow the declaration of any number
of mutually recursive procedures, each of possibly many arguments, as in exercise 3.21.
"""

#chap4
"""
Exercise 4.2 [*] Write down the specification for a zero?-exp.

Exercise 4.3 [*] Write down the specification for a call-exp.
(value-of exp1 env state0) ==> (val1 state1)
(value-of (call-exp exp exp1) env state0) ==> (val state2)

Exercise 4.4 [**] Write down the specification for a begin expresssion.
        Expression :: = begin Expression {; Expression} ∗ end
A begin expression may contain one or more subexpressions separated by semi-colons.
These are evaluated in order and the value of the last is returned.

Exercise 4.5 [**] Write down the specification for list (exercise 3.10).

Exercise 4.9 [*] Implement the store in constant time by representing it as a Scheme vector.
What is lost by using this representation?

Exercise 4.10 [*] Implement the begin expression as specified in exercise 4.4.

Exercise 4.11 [*] Implement list from exercise 4.5.

Exercise 4.12 [***] Our understanding of the store, as expressed in this interpreter,
dependson the meaning of effects in Scheme. In particular, it depends on us knowing
when these effects take place in a Scheme program. We can avoid this dependency by
writing an interpreter that more closely mimics the specification. In this interpreter,
value-of would return both a value and a store, just as in the specification.
A fragment of this interpreter appears in figure 4.6. We call this a store-passing interpreter.
Extend this interpreter to cover all of the language EXPLICIT-REFS.
Everyprocedurethat might modify the storereturns not just its usual value but also a
new store. These are packaged ina data type calledanswer. Complete this definition
of value-of.


Exercise 4.13 [***] Extend the interpreter of the preceding exercise to have procedures
of multiple arguments.

Exercise 4.17 [**] Write the rules for and implement multiargument procedures and
let expressions.

Exercise 4.18 [**] Write the rule for and implement multiprocedure letrec expressions.

Exercise 4.19 [**] Modify the implementation of multiprocedure letrec so that
each closure is built only once, and only one location is allocated for it.
This is like exercise 3.35.
"""



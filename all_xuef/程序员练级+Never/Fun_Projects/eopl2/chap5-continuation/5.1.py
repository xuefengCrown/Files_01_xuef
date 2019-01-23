
#5.1 A Continuation-Passing Interpreter
"""
Now, we know that an environment is a representation of a function from
symbols to denoted values.
What does a continuation represent?
The continuation of an expression represents a procedure that takes the result of the
expression and completes the computation.

So our interface must include a procedure apply-cont that takes a continuation cont
and an expressed value val and finishes the computation as specified by cont.
"""

# apply-cont: takes a continuation cont and an expressed value val
##and finishes the computation as specified by cont.
"""
FinalAnswer = ExpVal
apply-cont : Cont × ExpVal → FinalAnswer
"""

#What kind of continuation-builders will be included in the interface?


#value-of/k : Exp × Env × Cont → FinalAnswer
##3.Let us next consider a zero? expression.
"""
In a zero? expression, we want to evaluate the argument, and then return a value
to the continuation depending on the value of the argument.
So we evaluate the argument in a new continuation that will look at the returned value
and do the right thing.

So in value-of/k we write
(zero?-exp (exp1)
  (value-of/k exp1 env
    (zero1-cont cont)))

where (zero1-cont cont) is a continuation with the property that
(apply-cont (zero1-cont cont) val)
= (apply-cont cont
    (bool-val
      (zero? (expval->num val))))
"""

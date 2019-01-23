
#4.5.2 Lazy Evaluation: CALL-BY-NAME and CALL-BY-NEED
"""
All the parameter-passing mechanisms we have discussed so far are eager:
they always find a value for each operand.

We now turn to a very different form of parameter passing, called lazy evaluation.

Under lazy evaluation, an operand in a procedure call is not evaluated
until it is needed by the procedure body.
If the body never refers to the parameter, then there is no need to evaluate it.
"""

##We now modify our language to use lazy evaluation.
"""
Under lazy evaluation, we do not evaluate an operand expression until it is needed.
There-
fore we associate the bound variable of a procedure with an unevaluated operand.
When the procedure body needs the value of its bound variable, the associated operand is evaluated. 

Of course we will also have to include the environment in which that procedure is to be evaluated.
To do this, we introduce a new data type of thunks.
A thunk consists of an expression and an environment.
(define-datatype thunk thunk?
  (a-thunk
    (exp1 expression?)
    (env environment?)))

When a procedure needs to use the value of its bound variable,
it will evaluate the associated thunk.

Our situation is somewhat more complicated, because we need to accommodate
both lazy evaluation, effects, and eager evaluation (for let).

We therefore let our denoted values be references to locations containing either
expressed values or thunks.
    DenVal = Ref(ExpVal + Thunk)
    ExpVal = Int + Bool + Proc

Our policy for allocating new locations will be similar to the one we used for call-by-reference:
If the operand is a variable, then we pass its denotation, which is a reference.
Otherwise, we pass a reference to a new location containing a thunk for the unevaluated argument.

value-of-operand : Exp × Env → Ref
(define value-of-operand
  (lambda (exp env)
    (cases expression exp
      (var-exp (var) (apply-env env var))
      (else
        (newref (a-thunk exp env))))))
"""
##comments on lazy-evaluation
"""
An attraction of lazy evaluation in all its forms is that in the absence of
effects, it supports reasoning about programs in a particularly simple way.
The effect of a procedure call can be modeled by replacing the call with the
body of the procedure, with every reference to a formal parameter in the
body replaced by the corresponding operand. This evaluation strategy is the
basis for the lambda calculus, where it is called β -reduction.

Unfortunately, call-by-name and call-by-need make it difficult to determine
the order of evaluation, which in turn is essential to understanding
a program with effects. If there are no effects, though, this is not a problem.
Thus lazy evaluation is popular in functional programming languages (those
with no effects), and rarely found elsewhere.
"""





















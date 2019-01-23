# continuation-passing interpreter

#continuation 表示计算的剩余部分
#一个表达式的 continuation是一个过程，该过程接收这个表达式的值作为参数，然后完成剩余的计算。
##The continuation of an expression represents a procedure that
##takes the result of the expression and completes the computation.
"""
In our new interpreter, the major procedures such as eval-expression will take a third parameter.
This new parameter, the continuation, is intended to be an abstraction of the control
context in which each expression is evaluated. 

Our goal is to rewrite the interpreter so that no call to eval-expression builds control context:
all of the control context will be contained in the continuation parameter.


Now, we know that an environment is a representation of a function from symbols to locations.
What does a continuation represent? The continuation of an expression represents a procedure that
takes the result of the expression and completes the computation. So our interface must include a
procedure, apply-cont, that takes a continuation cont and an expressed value val and
finishes the computation as specified by cont.
"""
## const-exp
## var-exp
## letrec-exp
## zero?-exp
"""
In a zero? expression, we want to evaluate the argument, and then return a value
to the continuation depending on the value of the argument.
So we evaluate the argument in a new continuation that will look at the returned value
and do the right thing.

[zero?-exp (exp1)
           (value-of/k exp1 env
                       (zero1-cont cont))]
                           
(define (zero1-cont cont)
    (lambda (val)
        (apply-cont cont
            (bool-val
                (zero? (expval->num val))))))
"""
#xuef: (zero1-cont cont) is a continuation, 它会接收 exp1然后完成计算的剩余部分。
"""
where (zero1-cont cont) is a continuation with the property that
(apply-cont (zero1-cont cont) val)
= (apply-cont cont
    (bool-val
      (zero? (expval->num val))))
"""
#我们假设 exp1 = 1, 来推算一下
"""
exp = (zero? exp1)
:: (value-of/k exp env end-cont)
= (value-of/k exp1 env (lambda (val)
                         (apply-cont end-cont
                           (bool-val
                             (zero? (expval->num val))))))
= (apply-cont (lambda (val)
                 (apply-cont end-cont
                   (bool-val
                     (zero? (expval->num val)))))
               1)
= (apply-cont end-cont (bool-val (zero? 1)))
= #f
"""

#let-exp
"""
 The original code for let was
(let-exp (var exp1 body)
  (let ((val1 (value-of exp1 env)))
    (value-of body
      (extend-env var val1 env))))

In the continuation-passing interpreter, we need to evaluate exp1 in a context that
will finish the computation. So in value-of/k we write
(let-exp (var exp1 body)
  (value-of/k exp1 env
    (let-exp-cont var body env cont)))

;;(let-exp-cont var body env cont) 具有如下属性
(apply-cont (let-exp-cont var body env cont) val)
= (value-of/k body (extend-env var val env) cont)
"""
##This is another instance of the Tail Calls Don’t Grow the Continuation principle.???

#if-exp
"""
In an if expression, the first thing evaluated is the test, but the result of the test
is not the value of the entire expression. We need to build a new continuation that will
see if the result of the test expression is a true value, and evaluate either the true
expression or the false expression.

(if-exp (exp1 exp2 exp3)
  (value-of/k exp1 env
    (if-test-cont exp2 exp3 env cont)))

(apply-cont (if-test-cont exp2 exp3 env cont) val)
= (if (expval->bool val)
    (value-of/k exp2 env cont)
    (value-of/k exp3 env cont))
"""

#diff-exp
"""
they must evaluate both operands.

(diff-exp (exp1 exp2)
  (value-of/k exp1 env
    (diff1-cont exp2 env cont)))

When (diff1-cont exp2 env cont) receives a value, it should evaluate exp2 in a context
that saves the value of exp1. We specify this by writing
(apply-cont (diff1-cont exp2 env cont) val1)
= (value-of/k exp2 env
    (diff2-cont val1 cont))

When a (diff2-cont val1 cont) receives a value, we know the values of both operands
so we can proceed to send their difference to cont,which has been waiting to receive it.
The specification is
(apply-cont (diff2-cont val1 cont) val2)
= (let ((num1 (expval->num val1))
        (num2 (expval->num val2)))
    (apply-cont cont
      (num-val (- num1 num2))))
"""

#call-exp
"""
In the environment-passing interpreter, we wrote
(call-exp (rator rand)
  (let ((proc1 (expval->proc (value-of rator env)))
        (val (value-of rand env)))
    (apply-procedure proc1 val)))
Here we have two calls to consider, as we did in diff-exp. So we must
choose one of them to be first, and then we must transform the remainder
to handle the second. Furthermore, we will have to pass the continuation
to apply-procedure, because apply-procedure contains a call to value-of/k.

We choose the evaluation of the operator to be first, so in value-of/k we write
(call-exp (rator rand)
  (value-of/k rator env
    (rator-cont rand env cont)))

As with diff-exp, a rator-cont will evaluate the operand in a suitable continuation:
(apply-cont (rator-cont rand env cont) val1)
= (value-of/k rand env
    (rand-cont val1 cont))

When a rand-cont receives a value, it is ready to call the procedure:
(apply-cont (rand-cont val1 cont) val2)
= (let ((proc1 (expval->proc val1)))
    (apply-procedure/k proc1 val2 cont))

Last, we must modify apply-procedure to fit in this continuation-passing
style:
apply-procedure/k : Proc × ExpVal × Cont → FinalAnswer
(define apply-procedure/k
  (lambda (proc1 val cont)
    (cases proc proc1
      (procedure (var body saved-env)
        (value-of/k body
          (extend-env var val saved-env)
          cont)))))
"""
##???
"""
Now we can check the assertion that it is evaluation of actual parameters,
not the calling of procedures, that requires growing the control context.
In particular, if we evaluate a procedure call (exp1 exp2) in some continuation cont1,
the body of the procedure to which exp1 evaluates will also be evaluated in the continuation cont1.


But procedurecalls do not themselves grow control contexts.
Consider the evaluation of (exp1 exp2), where the value of exp1 is some procedure proc1
and the value of exp2 is some expressed value val2.
(value-of/k <<(exp1 exp2)>> ρ1 cont1)
= evaluate operator
(value-of/k <<exp1>> ρ1
  (rator-cont <<exp2>> ρ1 cont1))
  
= send the procedure to the continuation
(apply-cont
  (rator-cont <<exp2>> ρ1 cont1)
  proc1)
  
= evaluate the operand
(value-of/k <<exp2>> ρ1
  (rand-cont proc1 cont1))

= send the argument to the continuation
(apply-cont
  (rand-cont proc1 cont1)
  val2)
  
= apply the procedure
(apply-procedure/k proc1 val2 cont1)

So the procedure is applied, and its body is evaluated, in the same continuation
in which it was called. It is the evaluation of operands, not the entry
into a procedure body, that requires control context.
"""











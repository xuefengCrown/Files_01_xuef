
#3.3 PROC: A Language with Procedures
"""
For our interpreted language to be at all useful, we must allow
new procedures to be created. We call the new language PROC.
"""

##design
"""
We will follow the design of Scheme, and let procedures be expressed values
in our language, so that
    ExpVal = Int + Bool + Proc
    DenVal = Int + Bool + Proc
where Proc is a set of values representing procedures.

"""
##思考: procedure是什么?scheme的函数, java的函数。

#We will also need syntax for procedure creation and calling.
"""
    Expression :: = proc (Identifier) Expression
                        proc-exp (var body)
    Expression :: = (Expression Expression)
                        call-exp (rator rand)
"""

#Our next task is to determine what information must be included in a value
#representing a procedure.
##To do this, we consider what happens when we write a proc expression
##in an arbitrary position in our program.

##词法作用域
"""
let x = 200
in let f = proc (z) -(z,x)
   in let x = 100
      in let g = proc (z) -(z,x)
         in -((f 1), (g 1))

We conclude that the value of a proc expression must depend in some way
on the environment in which it is evaluated.
Therefore the constructor procedure must take three arguments:
the bound variable, the body, and the environment.
"""
#procedure call
"""
At a procedure call, we want to find the value of the operator and the operand.
If the value of the operator is a proc-val, then we want to apply it to
the value of the operand.

(value-of (call-exp rator rand) ρ)
= (let ((proc (expval->proc (value-of rator ρ)))
        (arg (value-of rand ρ)))
    (apply-procedure proc arg))

Herewe rely on a tester expval->proc, like expval->num, to test whether
the value of (value-of rator ρ), an expressed value, was constructed by
proc-val, and if so to extract the underlying procedure.
"""
##Last, we consider what happens when apply-procedureis invoked.
"""
As we have seen, the lexical scope rule tells us that when a procedure is applied,
its body is evaluated in an environment that binds the formal parameter of
the procedure to the argument of the call. Furthermore any other variables
must have the same values they had at procedure-creation time.
"""

##3.3.2 Representing Procedures
####一种有意思的方法
"""
proc? : SchemeVal → Bool
(define proc?
    (lambda (val)
        (procedure? val)))
        
procedure : Var × Exp × Env → Proc
(define procedure
    (lambda (var body env)
        (lambda (val)
            (value-of body (extend-env var val env)))))
            
apply-procedure : Proc × ExpVal → ExpVal
(define apply-procedure
    (lambda (proc1 val)
        (proc1 val)))
"""
####闭包
"""
proc? : SchemeVal → Bool

procedure : Var × Exp × Env → Proc
(define-datatype proc proc?
    (procedure
        (var identifier?)
        (body expression?)
        (saved-env environment?)))

apply-procedure : Proc × ExpVal → ExpVal
(define apply-procedure
    (lambda (proc1 val)
        (cases proc proc1
            (procedure (var body saved-env)
                (value-of body (extend-env var val saved-env))))))

These data structures are often called closures, because they are self-contained:
they contain everything the procedure needs in order to be applied.
We sometimes say the procedureis closed over or closed in its creation environment.
"""


































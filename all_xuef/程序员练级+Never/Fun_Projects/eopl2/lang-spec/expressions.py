
#支持的表达式
##concrete syntax
"""
Program :: = Expression
        a-program (exp1)
Expression :: = Number
        const-exp (num)
Expression :: = -(Expression , Expression)
        diff-exp (exp1 exp2)
Expression :: = zero? (Expression)
        zero?-exp (exp1)
Expression :: = if Expression then Expression else Expression
        if-exp (exp1 exp2 exp3)
Expression :: = Identifier
        var-exp (var)
Expression :: = let Identifier = Expression in Expression
        let-exp (var exp1 body)

Expression :: = proc (Identifier) Expression
        proc-exp (var body)
Expression :: = (Expression Expression)
        call-exp (rator rand)

let f = proc (x) -(x,11)
in (f (f 77))

Expression :: = letrec Identifier (Identifier) = Expression in Expression
        letrec-exp (p-name b-var p-body letrec-body)

Expression :: = begin Expression { ; Expression } ∗ end

Expression :: = newref (Expression)
        newref-exp (exp1)
Expression :: = deref (Expression)
        deref-exp (exp1)
Expression :: = setref (Expression , Expression)
        setref-exp (exp1 exp2)
"""
##abstract syntax

"""
(define-datatype program program?
  [a-program (exp1 expression?)])

(define-datatype expression expression?
  [const-exp (n number?)]
  [diff-exp (exp1 expression?)
            (exp2 expression?)]
  [zero?-exp
   (exp1 expression?)]
  [if-exp
   (test expression?)
   (then expression?)
   (else expression?)]
  [var-exp
   (var identifier?)]
  [let-exp
   (var identifier?)
   (exp1 expression?)
   (body expression?)]
  [emptylist-exp]
  [cons-exp (exp1 expression?) (exp2 expression?)]
  [null?-exp (exp expression?)]
  [car-exp (exp expression?)]
  [cdr-exp (exp expression?)]
  [proc-exp (var identifier?) (body expression?)]
  [call-exp (exp1 expression?) (exp2 expression?)]
  )
"""

##eval spec
"""
        (value-of exp1 ρ σ0) = (val1, σ1)
        (value-of exp2 ρ σ1) = (val2, σ2)
(value-of (diff-exp exp1 exp2) ρ σ0) = (val1 - val2, σ2)

p131 if-exp
"""

##ref exp
"""
if zero?(deref(x))
then 0
else 1
"""











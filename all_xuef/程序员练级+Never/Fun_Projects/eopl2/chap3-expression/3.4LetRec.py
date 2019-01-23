
#3.4 LETREC: A Language with Recursive Procedures
"""
We now define a new language LETREC, which adds recursion to our language.
"""

##syntax
"""
Expression :: = letrec Identifier (Identifier) = Expression in Expression
                    letrec-exp (p-name b-var p-body letrec-body)



letrec fact (x) = if zero?(x) then 1 else * (x, (fact sub1(x)))
in (fact 6)


"""

##
"""
(value-of
    (letrec-exp proc-name bound-var proc-body letrec-body)
    ρ)
= (value-of
    letrec-body
    (extend-env-rec proc-name bound-var proc-body ρ ))
"""

##?
"""
Here we have added a new procedure extend-env-rec to the environment interface.
But we still need to answer the question: What is the desired
behavior of (extend-env-rec proc-name bound-var proc-body ρ)?
"""

#We can implement extend-env-rec in any way that satisfies these requirements.


"""

(letrec-exp (proc-names idss bodies letrec-body)
  (eval-expression letrec-body
    (extend-env-recursively proc-names idss bodies env)))

;;comments on extend-env-recursively
In each of these implementations, we build a new closure each time a procedure is retrieved
from the environment. This is unnecessary since the environment for the closure is always the same.
If we use a ribcage representation like that of figure 2.4, we can build the closures only once,
by building an environment with a circular structure like that of figure 3.11.
"""    

##???
##Figure 3.12 Circular data structure representation of recursive environments
"""
(define extend-env-recursively
  (lambda (proc-names idss bodies old-env)
    (let ((len (length proc-names)))
      (let ((vec (make-vector len)))
        (let ((env (extended-env-record proc-names vec old-env)))
          (for-each (lambda (pos ids body)
                      (vector-set! vec pos (closure ids body env)))
                    (iota len) idss bodies) env)))))
                    
"""


























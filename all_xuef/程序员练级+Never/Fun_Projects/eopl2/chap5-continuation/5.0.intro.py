##cps intro 
"""
We will introduce the concept of a continuation as an abstraction of the control context,
and we will write interpreters that take a continuation as an argument, thus making the
control context explicit.

(define fact
  (lambda (n)
    (if (zero? n) 1 ( * n (fact (- n 1))))))
We can use a derivation to model a calculation with fact:
(fact 4)
= ( * 4 (fact 3))
= ( * 4 ( * 3 (fact 2)))
= ( * 4 ( * 3 ( * 2 (fact 1))))
= ( * 4 ( * 3 ( * 2 ( * 1 (fact 0)))))
= ( * 4 ( * 3 ( * 2 ( * 1 1))))
= ( * 4 ( * 3 ( * 2 1)))
= ( * 4 ( * 3 2))
= ( * 4 6)
= 24

Whydo these programs exhibit different control behavior? In the recursive
definition of factorial, the procedure fact is called in an operand position.
We need to save context around this call because we need to remember that after
the evaluation of the procedure call, we still need to finish evaluating the
operands and executing the outer call, in this case to the waiting multiplication.

"""

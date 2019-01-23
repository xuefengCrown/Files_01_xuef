
##fact
"""
(define fact/k
  (lambda (n cont)
    (if (zero? n)
      (cont 1)
      (fact/k (- n 1) (lambda (val) (cont ( * n val)))))))
We can read the definition of fact/k as:
If n is zero, send 1 to the continuation. Otherwise, evaluate fact of n − 1
in a continuation that calls the result val, and then sends to the continuation
the value (* n val).
"""

##fib
"""
(define fib
  (lambda (n)
    (fib/k n (lambda (val) val))))
(define fib/k
  (lambda (n cont)
    (if (< n 2)
        (cont 1)
        (fib/k (- n 1)
               (lambda (val1)
                 (fib/k (- n 2)
                        (lambda (val2)
                          (cont (+ val1 val2)))))))))
As we did for factorial, we can read this definition as
If n < 2, send 1 to the continuation. Otherwise, work on n − 1 in a
continuation that calls the result val1 and then works on n − 2 in a continuation
that calls the result val2 and then sends (+ val1 val2) to the continuation.
"""
##
"""
(define fact
  (lambda (n)
    (if (zero? n) 1 ( * n (fact (- n 1))))))
it is the position of the call to fact as an operand that requires the creation of a control context.

In general, we must understand the meaning of a language in order to
determine its tail positions. A subexpression in tail position has the property
that if it is evaluated, its value immediately becomes the value of the entire expression.

For a subexpression in tail position, no information need be saved,
and therefore no control context need be built.


"""





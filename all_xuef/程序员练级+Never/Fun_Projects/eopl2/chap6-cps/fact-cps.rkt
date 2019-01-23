
#lang eopl
(define (end-cont) (lambda (v) v))

(define (apply-cont cont v) (cont v))
(define (fact n)
  (fact/k n (end-cont)))

(define (fact/k n cont)
  (if (zero? n)
      (apply-cont cont 1)
      (fact/k (- n 1) (lambda (val)
                        (apply-cont cont (* n val))))
      ))

#|

  (fact/k 2 (end-cont))
= (fact/k 1 (lambda (val)
              (apply-cont end-cont (* 2 val))))
= (fact/k 0 (lambda (val)
               (apply-cont (lambda (val)
                             (apply-cont end-cont (* 2 val)))
                           (* 1 val))))
|#

(define (fct n)
  (fct-cps n (lambda (v) v)))

(define (fct-cps n k)
  (if (zero? n)
      (k 1)
      (fct-cps (- n 1) (lambda (v) (k (* n v))))))
#|
  (fct-cps 2 end-k)
= (fct-cps 1 (lambda (v) (end-k (* 2 v))))
= (fct-cps 0 (lambda (v)
               ((lambda (v) (end-k (* 2 v)))
                (* 1 v))))
= ((lambda (v)
    ((lambda (v) (end-k (* 2 v)))
     (* 1 v)))
   1)
|#

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

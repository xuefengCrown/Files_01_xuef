#lang eopl

; the data type of lambda-calculus expressions
(define-datatype lc-exp lc-exp?
  [var-exp
   (var symbol?)]
  [lambda-exp
   (bound-var symbol?)
   (body lc-exp?)]
  [app-exp
   (rator lc-exp?)
   (rand lc-exp?)])
;;This expression declares three constructors, var-exp, lambda-exp, and
;;app-exp, and a single predicate lc-exp?.

(define occurs-free?
  (lambda (search-var exp)
    (cases lc-exp exp
      (var-exp (var) (eqv? var search-var))
      (lambda-exp (bound-var body)
                  (and
                   (not (eqv? search-var bound-var))
                   (occurs-free? search-var body)))
      (app-exp (rator rand)
               (or
                (occurs-free? search-var rator)
                (occurs-free? search-var rand))))))

;; s-list
(define-datatype s-list s-list?
  (empty-s-list)
  (non-empty-s-list
   (first s-exp?)
   (rest s-list?)))
(define-datatype s-exp s-exp?
  (symbol-s-exp
   (sym symbol?))
  (s-list-s-exp
   (slst s-list?)))
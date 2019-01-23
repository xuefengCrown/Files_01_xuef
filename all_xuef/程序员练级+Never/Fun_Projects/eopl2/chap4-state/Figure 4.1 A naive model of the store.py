#Figure 4.1 A naive model of the store
"""
;;empty-store : () → Sto
(define empty-store
  (lambda () ’()))
  
usage: A Scheme variable containing the current state of the store.
Initially set to a dummy value.
(define the-store 'uninitialized)

;;get-store : () → Sto
(define get-store
  (lambda () the-store))

initialize-store! : () → Unspecified
usage: (initialize-store!) sets the-store to the empty store
(define initialize-store!
  (lambda ()
    (set! the-store (empty-store))))

reference? : SchemeVal → Bool
(define reference?
  (lambda (v)
    (integer? v)))

newref : ExpVal → Ref
(define newref
  (lambda (val)
    (let ((next-ref (length the-store)))
      (set! the-store (append the-store (list val)))
      next-ref)))

deref : Ref → ExpVal
(define deref
  (lambda (ref)
    (list-ref the-store ref)))

setref! : Ref × ExpVal → Unspecified
usage: sets the-store to a state like the original, but with position ref containing val.
(define setref!
  (lambda (ref val)
    (set! the-store
      (letrec
        ((setref-inner ;;usage: returns a list like store1, except that position ref1 contains val.
          (lambda (store1 ref1)
            (cond
              ((null? store1) (report-invalid-reference ref the-store))
              ((zero? ref1)
               (cons val (cdr store1)))
              (else
               (cons
                 (car store1)
                 (setref-inner
                   (cdr store1) (- ref1 1))))))))
        (setref-inner the-store ref)))))
"""
##comments on this implement
"""
This representation is extremely inefficient. Ordinary memory operations
require approximately constant time, but in our representation these operations
require time proportional to the size of the store.
No real implementation would ever do this, of course, but it suffices for our purposes.
"""










#lang plai
(define-type ArithExp
  [NumE (n number?)]
  [PlusE (l ArithExp?)
         (r ArithExp?)]
  [MultE (l ArithExp?)
         (r ArithExp?)])

(define (interp [ae ArithExp?])
  (type-case ArithExp ae
    [NumE (n) n]
    [PlusE (l r) (+ (interp l) (interp r))]
    [MultE (l r) (* (interp l) (interp r))]
    ))
;; calc (+ (* 3 3) (* 4 4))
(define e (PlusE
           (MultE
            (NumE 3) (NumE 3))
           (MultE
            (NumE 4) (NumE 4))))
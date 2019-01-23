#lang eopl

;20190104
;;> (product '(a b c) '(x y))
;;((a x) (a y) (b x) (b y) (c x) (c y))

(define (p-helper c sos)
  (map (lambda (ele) (list c ele)) sos))
(define (product sos1 sos2)
  (cond
    [(null? sos1) '()]
    [else (append (p-helper (car sos1) sos2)
                  (product (cdr sos1) sos2))]))

#|
> (path 17 '(14 (7 () (12 () ()))
(26 (20 (17 () ())
())
(31 () ()))))
(right left left)
|#
(define bst '(14 (7 () (12 () ()))
                 (26 (20 (17 () ())
                         ())
                     (31 () ()))))

(define (path n bst)
  (cond
    [(null? bst) '()]
    [(= n (car bst)) '()];n is found in the root
    [(> n (car bst)) (cons 'right (path n (caddr bst)))]
    [else (cons 'left (path n (cadr bst)))]
    ))
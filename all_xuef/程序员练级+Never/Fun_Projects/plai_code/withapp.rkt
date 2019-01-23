#lang plai
;; impl procedure call
(define-type ExprC
  [numC (n number?)]
  [idC (s symbol?)]
  [appC (fun symbol?) (arg ExprC?)]
  [plusC (l ExprC?) (r ExprC?)]
  [multC (l ExprC?) (r ExprC?)])

(define-type FunDefC
  [fdC (name symbol?)
       (arg symbol?)
       (body ExprC?)])

(define (subst old new e)
  (type-case ExprC e
    [numC (_) e]
    [idC (s) (cond
               [(symbol=? s old) new]
               [else e])]
    [appC (fun arg) (appC fun (subst old new arg))]
    [plusC (l r) (plusC (subst old new l)
                        (subst old new r))]
    [multC (l r) (multC (subst old new l)
                        (subst old new r))]))
(define (get-fundef n fds)
  (cond
    [(empty? fds) (error 'get-fundef "ref to undefined func")]
    [(cons? fds) (cond
                   [(equal? n (fdC-name (first fds))) (first fds)]
                   [else (get-fundef n (rest fds))])]))
(define (interp e fds)
  (type-case ExprC e
    [numC (n) n]
    [idC (_) (error 'interp "shouldn't get here")]
    [appC (fun arg) (let ([fd (get-fundef fun fds)])
                      (interp (subst (fdC-arg fd)
                                     arg
                                     (fdC-body fd))
                              fds))]
    [plusC (l r) (+ (interp l fds) (interp r fds))]
    [multC (l r) (* (interp l fds) (interp r fds))]
    ))
;(define (double x) (+ x x))
(define f1 (fdC 'double 'x (plusC (idC 'x) (idC 'x))))
;(define (quadruple x) (double (double x)))
(define f2 (fdC 'quadruple 'x (appC 'double (appC 'double (idC 'x)))))
;(define (const5 _) 5)
;(fdC 'const5 '_ (numC 5))
(define fds (list f1 f2))
(define app (appC 'quadruple (numC 3)))
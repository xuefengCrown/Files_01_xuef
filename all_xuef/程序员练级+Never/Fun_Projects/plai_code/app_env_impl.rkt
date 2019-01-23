#lang plai
; Environments
(define-type Binding
  [bind (name symbol?) (val number?)])
;;env-helper
;; Env listof-Binding
(define mt-env empty)
(define extend-env cons)
(define (lookup s env)
  (cond [(empty? env) (error 'lookup "name not found")]
        [(symbol=? s (bind-name (car env))) (bind-val (car env))]
        [else (lookup s (cdr env))]
        ))
; Expression
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
;func-name-->func-def
(define (get-fundef n fds)
  (cond
    [(empty? fds) (error 'get-fundef "ref to undefined func")]
    [(cons? fds) (cond
                   [(equal? n (fdC-name (first fds))) (first fds)]
                   [else (get-fundef n (rest fds))])]))
(define (interp e env fds)
  (type-case ExprC e
    [numC (n) n]
    [idC (s) (lookup s env)]
    [appC (f a) (let ([fd (get-fundef f fds)])
                  (interp (fdC-body fd)
                          (extend-env (bind (fdC-arg fd)
                                            (interp a env fds))
                                      env);is known as dynamic scope
                          fds))]
    [plusC (l r) (+ (interp l env fds) (interp r env fds))]
    [multC (l r) (* (interp l env fds) (interp r env fds))]
    )
  )

;test
(test (interp (plusC (numC 10) (appC 'const5 (numC 10)))
              mt-env
              (list (fdC 'const5 '_ (numC 5))))
      15)
 
(test (interp (plusC (numC 10) (appC 'double (plusC (numC 1) (numC 2))))
              mt-env
              (list (fdC 'double 'x (plusC (idC 'x) (idC 'x)))))
      16)
 
(test (interp (plusC (numC 10) (appC 'quadruple (plusC (numC 1) (numC 2))))
              mt-env
              (list (fdC 'quadruple 'x (appC 'double (appC 'double (idC 'x))))
                    (fdC 'double 'x (plusC (idC 'x) (idC 'x)))))
      22)
#lang plai
; Environments
(define-type Binding
  [bind (name symbol?) (val Value?)])
;;env-helper
;; Env listof-Binding
(define mt-env empty)
(define extend-env cons)
(define (lookup s env)
  (cond [(empty? env) (error 'lookup "name not found")]
        [(symbol=? s (bind-name (car env))) (bind-val (car env))]
        [else (lookup s (cdr env))]))

; Expression
(define-type ExprC
  [numC (n number?)]
  [idC (s symbol?)]
  [lamC (arg symbol?) (body ExprC?)]
  [appC (fun ExprC?) (arg ExprC?)]
  [plusC (l ExprC?) (r ExprC?)]
  [multC (l ExprC?) (r ExprC?)])

(define-type Value
  [numV (n number?)]
  [closV (arg symbol?) (body ExprC?) (env list?)])

(define (num+ [l Value?] [r Value?])
  (cond
    [(and (numV? l) (numV? r))
     (numV (+ (numV-n l) (numV-n r)))]
    [else
     (error 'num+ "one argument was not a number")]))
(define (num* [l Value?] [r Value?])
  (cond
    [(and (numV? l) (numV? r))
     (numV (* (numV-n l) (numV-n r)))]
    [else
     (error 'num* "one argument was not a number")]))

;;-->Value
(define (interp e env)
  (type-case ExprC e
    [numC (n) (numV n)]
    [idC (s) (lookup s env)]
    [lamC (a b) (closV a b env)]
    [appC (f a) (let ([fd (interp f env)])
                  (interp (closV-body fd)
                          (extend-env (bind (closV-arg fd)
                                            (interp a env))
                                      (closV-env fd))
                          ))]
    [plusC (l r) (num+ (interp l env) (interp r env))]
    [multC (l r) (num* (interp l env) (interp r env))]
    )
  )

;test

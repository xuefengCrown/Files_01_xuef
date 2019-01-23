#lang eopl

(define scheme-value? (lambda (s) #t))

; 如何确定各变种?根据BNF语法?
; 能采取统一动作，就可以作为一类?
; Java中如何确定接口和各实现类?
(define-datatype Env Env?
  [mt-env]
  [extend-env (save-var symbol?)
              (save-val scheme-value?)
              (saved-env Env?)])

(define report-no-binding-found
  (lambda (search-var)
    (eopl:error 'apply-env "No binding for ~s" search-var)))

(define (apply-env env search-var)
  (cases Env env
    [mt-env () (report-no-binding-found search-var)]
    [extend-env (var val saved-env)
                (if (eqv? var search-var)
                    val
                    (apply-env saved-env search-var))]))
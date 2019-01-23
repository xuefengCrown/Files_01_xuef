#lang eopl

;(require "env.rkt")
;parser
;;(scan&parse "-(55, -(x,11))")
(define the-grammar
  '((program (expression) a-program)
    (expression (number) const-exp)
    ;(expression ("+" "(" expression "," expression ")") plus-exp)
    (expression ("-" "(" expression "," expression ")") diff-exp)
    ;(expression ("*" "(" expression "," expression ")") mul-exp)
    ;(expression ("/" "(" expression "," expression ")") div-exp)
    (expression ("zero?" "(" expression ")") zero?-exp)
    ;(expression ("equal?" "(" expression "," expression ")") equal?-exp)
    ;(expression ("greater?" "(" expression "," expression ")") greater?-exp)
    ;(expression ("less?" "(" expression "," expression ")") less?-exp)
    (expression ("if" expression "then" expression "else" expression) if-exp)
    (expression (identifier) var-exp)
    (expression ("let" identifier "=" expression "in" expression) let-exp)
    ;(expression ("minus" "(" expression ")") minus-exp)
    (expression ("cons" "(" expression "," expression ")") cons-exp)
    (expression ("car" "(" expression ")") car-exp)
    (expression ("cdr" "(" expression ")") cdr-exp)
    (expression ("null?" "(" expression ")") null?-exp)
    (expression ("emptylist") emptylist-exp)
    ;;new stuff
    ;(expression ("letproc" identifier "=" "(" identifier ")" expression "in" expression) let-proc-exp)
    ;(expression ("(" expression expression ")") call-exp)
    ))
(define the-lexical-spec
  '((whitespace (whitespace) skip)
    (comment ("%" (arbno (not #\newline))) skip)
    (identifier
     (letter (arbno (or letter digit "_" "-" "?")))
     symbol)
    (number (digit (arbno digit)) number)
    (number ("-" digit (arbno digit)) number)))
(define scan&parse
    (sllgen:make-string-parser the-lexical-spec the-grammar))


;Syntax data types for the LET language
(define-datatype program program?
  [a-program (exp1 expression?)])

(define-datatype expression expression?
  [const-exp (n number?)]
  [diff-exp (exp1 expression?)
            (exp2 expression?)]
  [zero?-exp
   (exp1 expression?)]
  [if-exp
   (test expression?)
   (then expression?)
   (else expression?)]
  [var-exp
   (var identifier?)]
  [let-exp
   (var identifier?)
   (exp1 expression?)
   (body expression?)]
  [emptylist-exp]
  [cons-exp (exp1 expression?) (exp2 expression?)]
  [null?-exp (exp expression?)]
  [car-exp (exp expression?)]
  [cdr-exp (exp expression?)]
  )

(define identifier? symbol?)

;Expressed values for the LET language
(define-datatype expval expval?
  [num-val
   (num number?)]
  [bool-val
   (bool boolean?)]
  [emptylist-val]
  [cons-val (first expval?) (rest expval?)])
;;expval->num : ExpVal → Int
(define expval->num
  (lambda (val)
    (cases expval val
      (num-val (num) num)
      (else (report-expval-extractor-error 'num val)))))
;;expval->bool : ExpVal → Bool
(define expval->bool
  (lambda (val)
    (cases expval val
      (bool-val (bool) bool)
      (else (report-expval-extractor-error 'bool val)))))

(define expval->car
  (lambda (val)
    (cases expval val
      (cons-val (first rest) first)
      (else (report-expval-extractor-error 'cons val)))))

(define expval->cdr
  (lambda (val)
    (cases expval val
      (cons-val (first rest) rest)
      (else (report-expval-extractor-error 'cons val)))))

(define (expval->emptylist? val)
    (cases expval val
      (emptylist-val () #t)
      (cons-val (first rest) #f)
      (else (report-expval-extractor-error 'cons-or-emptylist val))))
(define report-expval-extractor-error
  (lambda (type val)
    (eopl:error 'extract "can't extract val for ~s" type)))

;environment
(define scheme-value? (lambda (s) #t))
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
					
;;init-env
(define init-env
    (extend-env
     'i (num-val 1)
     (extend-env
      'v (num-val 5)
      (extend-env
       'x (num-val 10)
       (mt-env)))))

;Interpreter for the LET language
;;run : String → ExpVal
(define (run code_str)
  (value-of-program (scan&parse code_str)))
;;value-of-program : Program → ExpVal
(define (value-of-program pgm)
  (cases program pgm
    [a-program (exp1) (value-of exp1 init-env)]))
;;value-of : Exp × Env → ExpVal
(define (value-of exp env)
  (cases expression exp
    [const-exp (n) (num-val n)]
    [var-exp (var) (apply-env env var)]
    [diff-exp (exp1 exp2)
              (let ((val1 (value-of exp1 env))
                    (val2 (value-of exp2 env)))
                (let ((num1 (expval->num val1))
                      (num2 (expval->num val2)))
                  (num-val (- num1 num2))))]
    [zero?-exp (exp1) (let ((val1 (value-of exp1 env)))
                        (let ((num1 (expval->num val1)))
                          (if (zero? num1)
                              (bool-val #t)
                              (bool-val #f))))]
    [if-exp (test then else) (let ((test-v (expval->bool (value-of test env))))
                               (if test-v
                                   (value-of then env)
                                   (value-of else env)))]
    [let-exp (var exp1 body) (let ((v (value-of exp1 env)))
                               (value-of body (extend-env var v env)))]
    [emptylist-exp () (emptylist-val)]
    [cons-exp (exp1 exp2) (let ((v1 (value-of exp1 env))
                                (v2 (value-of exp2 env)))
                            (cons-val v1 v2))]
    [car-exp (e) (let ((ev (value-of e env)))
                   (expval->car ev))]
    [cdr-exp (e) (let ((ev (value-of e env)))
                   (expval->cdr ev))]
    [null?-exp (e) (let ((v (value-of e env)))
                     (let ((b (expval->emptylist? v)))
                       (bool-val b)))]
    ))

;;test
#|
(run "let x = 4 in -(x,1)")
(prettyp (run "let x = 4 in cons(x, cons(cons(-(x,1), emptylist), emptylist))"))
|#

;; QAQ
#|
为什么要用 num-val, bool-val来对结果值进行包装?
|#

; ------------------------------------------------------------------------------
; A nice REPL for interactive use


;;心得
#|
数据结构就是一种 构造/提取的约定或协议。比如 cons
只要满足:
car(cons a b) = a
cdr(cons a b) = b
那就是合格的 cons
|#

;; pretty-print
(define (prettyp v)
  (cases expval v
    [num-val (n) n]
    [bool-val (b) b]
    [emptylist-val () '()]
    [cons-val (e1 e2) (cons (prettyp e1) (prettyp e2))]
    ))
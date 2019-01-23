#lang eopl
(require "state.rkt")
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
    (expression ("list" "(" (separated-list expression ",") ")") list-exp)
    ;;procedure
    (expression ("proc" "(" identifier ")" expression) proc-exp)
    (expression ("(" expression expression ")") call-exp)
    ;(expression ("letrec"  (arbno identifier "(" identifier ")" "=" expression) "in" expression) letrec-exp)

    ;; new stuff
    (expression ("begin" expression (arbno ";" expression) "end") begin-exp)

    ;newref (Expression)
    (expression ("newref" "(" expression ")") newref-exp)
    (expression ("deref" "(" expression ")") deref-exp)
    (expression ("setref" "(" expression "," expression ")") setref-exp)
    ))
(define the-lexical-spec
  '((whitespace (whitespace) skip)
    (comment ("%" (arbno (not #\newline))) skip)
    (identifier
     (letter (arbno (or letter digit "_" "-" "?")))
     symbol)
    (number (digit (arbno digit)) number)
    (number ("-" digit (arbno digit)) number)))


;Syntax data types for the language
;;;;;;;;;;;;;;;; sllgen boilerplate ;;;;;;;;;;;;;;;;

(sllgen:make-define-datatypes the-lexical-spec the-grammar)

(define show-the-datatypes
  (lambda () (sllgen:list-define-datatypes the-lexical-spec the-grammar)))

(define scan&parse
    (sllgen:make-string-parser the-lexical-spec the-grammar))
#|
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
  [proc-exp (var identifier?) (body expression?)]
  [call-exp (exp1 expression?) (exp2 expression?)]
  [newref-exp (exp expression?)]
  [deref-exp (exp expression?)]
  [setref-exp (exp1 expression?) (exp2 expression?)])
|#
(define identifier? symbol?)

;environment
(define scheme-value? (lambda (s) #t))
(define-datatype Env Env?
  [mt-env]
  [extend-env (save-var symbol?)
              (save-val scheme-value?)
              (saved-env Env?)]
  [extend-env-rec (p-name identifier?)
                  (b-var identifier?)
                  (body expression?)
                  (env Env?)])

(define report-no-binding-found
  (lambda (search-var)
    (eopl:error 'apply-env "No binding for ~s" search-var)))

(define (apply-env env search-var)
  (cases Env env
    [mt-env () (report-no-binding-found search-var)]
    [extend-env (var val saved-env)
                (if (eqv? var search-var)
                    val
                    (apply-env saved-env search-var))]
    [extend-env-rec (p-name b-var p-body saved-env)
                    (if (eqv? search-var p-name)
                        (proc-val (procedure b-var p-body env));;???
                        (apply-env saved-env search-var))]))
					

;procedure
(define-datatype proc proc?
  (procedure
   (var identifier?)
   (body expression?)
   (saved-env Env?)))

;Exressed value and denoted value
(define-datatype expval expval?
  [num-val
   (num number?)]
  [bool-val
   (bool boolean?)]
  [emptylist-val]
  [cons-val (first expval?) (rest expval?)]
  [proc-val (p proc?)]
  [ref-val (ref reference?)])

;;init-env
(define init-env
    (extend-env
     'i (num-val 1)
     (extend-env
      'v (num-val 5)
      (extend-env
       'x (num-val 10)
       (mt-env)))))

;;expval->proc
(define (expval->proc val)
  (cases expval val
    [proc-val (p) p]
    [else (report-expval-extractor-error 'proc val)]))
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

(define expval->ref
  (lambda (v)
    (cases expval v
	   (ref-val (ref) ref)
	   (else (report-expval-extractor-error 'reference v)))))

(define report-expval-extractor-error
  (lambda (type val)
    (eopl:error 'extract "can't extract val for ~s" type)))

;Interpreter for the LET language
;;run : String → ExpVal
(define (run code_str)
  (value-of-program (scan&parse code_str)))
;;value-of-program : Program → ExpVal
(define (value-of-program pgm)
  (initialize-store!);;
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
    [proc-exp (var body) (proc-val (procedure var body env))]
    [call-exp (e1 e2) (let ([p (expval->proc (value-of e1 env))]
                            [arg (value-of e2 env)])
                        (apply-proc p arg))]
    [list-exp (alist)
                (if (null? alist) (emptylist-val)
                    (cons-val
                     (value-of (car alist) env)
                     (value-of (list-exp (cdr alist)) env)))]
    [begin-exp (exp1 exps)
               (letrec
                   ((value-of-begins
                     (lambda (e1 es)
                       (let ((v1 (value-of e1 env)))
                         (if (null? es)
                             v1
                             (value-of-begins (car es) (cdr es)))))))
                 (value-of-begins exp1 exps))]
    [newref-exp (exp1)
                (let ((v1 (value-of exp1 env)))
                  (ref-val (newref v1)))]

    [deref-exp (exp1)
               (let ((v1 (value-of exp1 env)));v1 should be a ref-val
                 (let ((ref1 (expval->ref v1)))
                   (deref ref1)))]

    [setref-exp (exp1 exp2)
                (let ((ref (expval->ref (value-of exp1 env))))
                  (let ((val2 (value-of exp2 env)))
                    (begin
                      (setref! ref val2)
                      (num-val 23))))]
    ))
(define (apply-proc p arg)
  (cases proc p
    [procedure (var body saved-env)
               (value-of body (extend-env var arg saved-env))]))

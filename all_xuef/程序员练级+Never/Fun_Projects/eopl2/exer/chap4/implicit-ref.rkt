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
    (expression ("letrec"  (arbno identifier "(" identifier ")" "=" expression) "in" expression) letrec-exp)

    ;; new stuff
    (expression ("begin" expression (arbno ";" expression) "end") begin-exp)
    ;;assignment
    (expression ("set" identifier "=" expression) set-exp)
    ))
(define the-lexical-spec
  '((whitespace (whitespace) skip)
    (comment ("%" (arbno (not #\newline))) skip)
    (identifier
     (letter (arbno (or letter digit "_" "-" "?")))
     symbol)
    (number (digit (arbno digit)) number)
    (number ("-" digit (arbno digit)) number)))
;;;;;;;;;;;;;;;; sllgen boilerplate ;;;;;;;;;;;;;;;;
(sllgen:make-define-datatypes the-lexical-spec the-grammar)

(define show-the-datatypes
  (lambda () (sllgen:list-define-datatypes the-lexical-spec the-grammar)))

(define scan&parse
    (sllgen:make-string-parser the-lexical-spec the-grammar))

;environment
(define identifier? symbol?)
(define scheme-value? (lambda (s) #t))
(define-datatype Env Env?
  [mt-env]
  [extend-env (save-var symbol?)
              (loc scheme-value?)
              (saved-env Env?)]
  [extend-env-rec*
   (proc-names (list-of symbol?))
   (b-vars (list-of symbol?))
   (proc-bodies (list-of expression?))
   (saved-env Env?)])

(define report-no-binding-found
  (lambda (search-var)
    (eopl:error 'apply-env "No binding for ~s" search-var)))

(define (apply-env env search-var)
  (cases Env env
    [mt-env () (report-no-binding-found search-var)]
    [extend-env (var loc saved-env)
                (if (eqv? var search-var)
                    loc
                    (apply-env saved-env search-var))]
    [extend-env-rec* (p-names b-vars p-bodies saved-env)
                    (let ((n (location search-var p-names)))
                      (if n
                          (newref
                           (proc-val
                            (procedure
                             (list-ref b-vars n)
                             (list-ref p-bodies n)
                             env)))
                          (apply-env saved-env search-var)))]))
(define location
  (lambda (sym syms)
    (cond
     ((null? syms) #f)
     ((eqv? sym (car syms)) 0)
     ((location sym (cdr syms))
      => (lambda (n)
           (+ n 1)))
     (else #f))))					

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

(define init-env (mt-env))

;interp
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
    [const-exp (n) (num-val n)];?
    ;The environment now always binds variables to locations,
    ;so when a variable appears as an expression, we need to dereference it
    [var-exp (var) (deref (apply-env env var))]
    [set-exp (var exp) (let ([rv (value-of exp env)]
                             [loc (apply-env env var)])
                         (begin (setref! loc rv)
                                (num-val 100)))]
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
                               (value-of body
                                         (extend-env var (newref v) env)))]
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
    [letrec-exp (p-names b-vars p-bodies letrec-body)
                  (value-of letrec-body
                            (extend-env-rec* p-names b-vars p-bodies env))]
    ))

(define (apply-proc p arg)
  (cases proc p
    [procedure (var body saved-env)
               (value-of body (extend-env var (newref arg) saved-env))]))

#|
In this design, every variable denotes a reference.

Locations are created with each binding operation: at each procedure call, let, or letrec.
We also need to rewrite the rules for procedure call and let to show the modified store.
|#
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
    ;(expression ("set" identifier "=" expression) set-exp)
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
  [extend-env-rec
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
    [extend-env-rec (p-names b-vars p-bodies saved-env)
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

;cont
;; end-cont : () -> Cont
(define end-cont
  (lambda ()
    (lambda (val)
      (begin
        (eopl:printf "End of computation.~%")
        val))))
;interp
;;run : String → ExpVal
(define (run code_str)
  (value-of-program (scan&parse code_str)))
;;value-of-program : Program → ExpVal
(define value-of-program
  (lambda (pgm)
    (cases program pgm
      (a-program (exp1)
                 (value-of/k exp1 (init-env) (end-cont))))))

;;value-of/k : Exp × Env × Cont → FinalAnswer
(define (value-of/k exp env cont)
  (cases expression exp
    [const-exp (num) (apply-cont cont (num-val num))]
    [var-exp (var) (apply-cont cont (apply-env env var))]
    [zero?-exp (exp1)
               (value-of/k exp1 env
                           (zero1-cont cont))]
    [let-exp (var exp1 body)
             (value-of/k exp1 env
                         (let-exp-cont var body env cont))]
    [if-exp (exp1 exp2 exp3)
            (value-of/k exp1 env
                        (if-test-cont exp2 exp3 env cont))]
    ))

;; end-cont : () -> Cont
(define end-cont
  (lambda ()
    (lambda (val)
      (begin
        (eopl:printf "End of computation.~%")
        val))))
;;(zero1-cont cont) is a continuation
(define zero1-cont
      (lambda (cont)
        (lambda (val)
          (apply-cont cont
                      (bool-val
                       (zero? (expval->num val)))))))
;; let-exp-cont : Var * Exp * Env * Cont -> Cont
(define let-exp-cont
  (lambda (var body env cont)
    (lambda (val)
      (value-of/k body (extend-env var val env) cont))))
;; if-test-cont : Exp * Exp * Exp * Cont -> Cont
(define if-test-cont
  (lambda (exp2 exp3 env cont)
    (lambda (val)
      (if (expval->bool val)
          (value-of/k exp2 env cont)
          (value-of/k exp3 env cont)))))

(define apply-cont
  (lambda (cont v)
    (cont v)))

;;;;	(load "C:\\code_dxf\\xuefgit\\Files_01_xuef\\all_xuef\\SICP\\code_book\\sicp_interpreter.scm")
;;; 4.1
;;;; helper
(define (cadr s) (car (cdr s)))
(define (cddr s) (cdr (cdr s)))
(define (caddr s) (car (cdr (cdr s))))
(define (cadddr s) (car (cdr (cdr (cdr s)))))
(define (caadr s) (car (car (cdr s))))
(define (cdadr s) (cdr (car (cdr s))))
;;;; helper

(define (_eval_ exp env)
	(cond ((self-evaluating? exp) exp)
		  ((variable? exp) (lookup-variable-value exp env))
		  ((quoted? exp) (text-of-quotation exp))
		  ((assignment? exp) (eval-assignment exp env))
		  ((definition? exp) (eval-definition exp env))
		  ((if? exp) (eval-if exp env))
		  ((and-exp? exp) (eval-and (and-exps exp) env))
		  ((let-exp? exp) (_eval_ (let->combination exp) env))
		  ((let*? exp) (_eval_ (let*->nested-lets exp) env))
		  ((lambda? exp)
				(make-procedure (lambda-parameters exp)
								(lambda-body exp)
								env))
		  ((begin? exp) (eval-sequence (begin-actions exp) env))
		  ((cond? exp) (_eval_ (cond-if exp) env))
		  ((application? exp) 
				(_apply_ (_eval_ (operator exp) env) 
							 (list-of-values (operands exp) env)))
		  (else (error "Unknown expression type -- EVAL" exp))))

(define (_apply_ procedure arguments)
	(cond ((primitive-procedure? procedure) 
				(apply-primitive-procedure procedure arguments))
		  ((compound-procedure? procedure) 
				(eval-sequence (procedure-body procedure)
							   (extend-environment (procedure-parameters procedure)
												   arguments
												   (procedure-environment procedure))))
		  (else (error "Unknown expression type -- APPLY" exp))))

		  
;;;; 求值过程参数
(define (list-of-values exps env)
	(if (no-operands? exps)
		'()
		(cons (_eval_ (first-operand exps) env)
			  (list-of-values (rest-operands exps) env))))	  
		  
;;;; 条件
(define (eval-if exp env)
	(if (true? (_eval_ (if-predicate exp) env))
		(_eval_ (if-consequent exp) env)
		(_eval_ (if-alternative exp) env)))
		
;;;; 序列
(define (eval-sequence exps env)
  (cond ((last-exp? exps) (_eval_ (first-exp exps) env))
        (else (_eval_ (first-exp exps) env)
              (eval-sequence (rest-exps exps) env))))
		
;;;; Assignments and definitions
(define (eval-assignment exp env)
	(set-variable-value! (assignment-variable exp)
						 (_eval_ (assignment-value exp) env)
						 env)
	'ok)	
	
(define (eval-definition exp env)
  (define-variable! (definition-variable exp)
                    (_eval_ (definition-value exp) env)
                    env)
  (definition-variable exp))	;; 'ok

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;  eval-and
;; (and (>= x 60) (<= x 80))
(define (and-exp? exp) (tagged-list? exp 'and))
(define (and-exps exp) (cdr exp))

(define (eval-and exps env)
    (cond ((null? exps) #t)
          ((last-exp? exps)
            (_eval_ (first-exp exps) env))
          ((true? (_eval_ (first-exp exps) env))
            (eval-and (rest-exps exps) env))
          (else #f)))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; let-exp: (let ((x 1) (y 2)) body)
;; let表达式可以转化为 对组合式的求值
(define (let-exp? exp) (tagged-list? exp 'let))

(define (let-vars exp) (map (lambda (pair) (car pair)) (cadr exp)))
(define (let-vals exp) (map (lambda (pair) (cadr pair)) (cadr exp)))
(define (let-body exp) (cddr exp))

;;;; 将let表达式规约为 组合式的求值
(define (let->combination exp)
	(cons (make-lambda 
			(let-vars exp) 
			(let-body exp))
		  (let-vals exp)))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; let*
;;;; (let* ((x 3) (y (+ x 2))) (* x y))
(define (let*? exp) (tagged-list? exp 'let*))
(define (let-args exp) (cadr exp)) 
(define (let-body exp) (cddr exp)) 
(define (make-let args body) (cons 'let (cons args body))) 
  
(define (let*->nested-lets exp) 
   (define (reduce-let* args body) 
     (if (null? args) 
         (sequence->exp body)
         (make-let (list (car args)) 
                   (list (reduce-let* (cdr args) body))))) 
   (reduce-let* (let-args exp) (let-body exp))) 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		  
;; 语言的语法规范
;;;; 自求值表达式只有数和字符串 1 "hello"
(define (self-evaluating? exp)
	(cond ((number? exp) true)
		  ((string? exp) true)
		  (else false)))
;;;; Variables are represented by symbols
(define (variable? exp) (symbol? exp))

;;;; Quotations have the form (quote <text-of-quotation>)
(define (quoted? exp)
	(tagged-list? exp 'quote))
	
	;;;; 确定一个表的开始是不是某个给定符号
(define (tagged-list? exp tag)
	(if (pair? exp)
		(eq? (car exp) tag)
		false))	
(define (text-of-quotation exp) (cadr exp))

;;;; 赋值的形式是 (set! <var> <value>)
(define (assignment? exp) (tagged-list? exp 'set!))
(define (assignment-variable exp) (cadr exp))
(define (assignment-value exp) (caddr exp))

;;;; Definitions have the form
;;;; (define <var> <value>)
;;;; or the form
;;;; (define (<var> <parameter1> ... <parametern>) 这种是过程定义
;;;; 	<body>)
(define (definition? exp) (tagged-list? exp 'define))

;; (define var 1)
;; (define (f var) (<body>))
(define (definition-variable exp)
	(if (symbol? (cadr exp))
		(cadr exp)
		(caadr exp)))
(define (definition-value exp)
	(if (symbol? (cadr exp))
		(caddr exp)
		(make-lambda (cdadr exp) (cddr exp))))
		
;;;; lambda表达式是由符号lambda开始的表
(define (lambda? exp) (tagged-list? exp 'lambda))
(define (lambda-parameters exp) (cadr exp))
(define (lambda-body exp) (cddr exp))

(define (make-lambda parameters body) (cons 'lambda (cons parameters body)))

;;;; Conditionals begin with if and have a predicate, a consequent, and an (optional) alternative. 
;;;; If the expression has no alternative part, we provide false as the alternative.
(define (if? exp) (tagged-list? exp 'if))
(define (if-predicate exp) (cadr exp))
(define (if-consequent exp) (caddr exp))
(define (if-alternative exp)
	(if (not (null? (caddr exp)))
		(cadddr exp)
		'false))
;;;; 构造 if 表达式, 在cond-if里使用, 用于将cond表达式变换为if表达式
(define (make-if predicate consequent alternative)
	(list 'if predicate consequent alternative))
	
;;;; begin 包装起一个表达式序列
(define (begin? exp) (tagged-list? exp 'begin))
(define (begin-actions exp) (cdr exp))
(define (last-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))

;;;; 将序列变换为一个表达式 '(exp1 exp2)--> (begin exp1 exp2); '(exp1)-->exp1
(define (sequence->exp seq)
  (cond ((null? seq) seq)
        ((last-exp? seq) (first-exp seq))
        (else (make-begin seq))))
(define (make-begin seq) (cons 'begin seq))

;;;; A procedure application is any compound expression that is not one of the above expression types. 
;;;; The car of the expression is the operator, and the cdr is the list of operands
(define (application? exp) (pair? exp))
(define (operator exp) (car exp))
(define (operands exp) (cdr exp))
(define (no-operands? ops) (null? ops))
(define (first-operand ops) (car ops))
(define (rest-operands ops) (cdr ops))


;;;; 
(define (cond? exp) (tagged-list? exp 'cond))
(define (cond-clauses exp) (cdr exp))
(define (cond-else-clause? clause)
  (eq? (cond-predicate clause) 'else))
(define (cond-predicate clause) (car clause))
(define (cond-actions clause) (cdr clause))
(define (cond->if exp)
  (expand-clauses (cond-clauses exp)))

(define (expand-clauses clauses)
  (if (null? clauses)
      'false                          ; no else clause
      (let ((first (car clauses))
            (rest (cdr clauses)))
        (if (cond-else-clause? first)
            (if (null? rest)
                (sequence->exp (cond-actions first))
                (error "ELSE clause isn't last -- COND->IF"
                       clauses))
            (make-if (cond-predicate first)
                     (sequence->exp (cond-actions first))
                     (expand-clauses rest))))))


;; Evaluator Data Structures
;;;; 谓词检测
(define (true? x)
  (not (eq? x false)))
(define (false? x)
  (eq? x false))
  
;;;; 复合过程
(define (make-procedure parameters body env)
  (list 'procedure parameters body env))
(define (compound-procedure? p)
  (tagged-list? p 'procedure))
(define (procedure-parameters p) (cadr p))
(define (procedure-body p) (caddr p))
(define (procedure-environment p) (cadddr p))  

;;;; 环境
(define (enclosing-environment env) (cdr env))
(define (first-frame env) (car env))
(define the-empty-environment '())

(define (make-frame variables values)
  (cons variables values))
(define (frame-variables frame) (car frame))
(define (frame-values frame) (cdr frame))
(define (add-binding-to-frame! var val frame)
  (set-car! frame (cons var (car frame)))
  (set-cdr! frame (cons val (cdr frame))))

(define (extend-environment vars vals base-env)
  (if (= (length vars) (length vals))
      (cons (make-frame vars vals) base-env)
      (if (< (length vars) (length vals))
          (error "Too many arguments supplied" vars vals)
          (error "Too few arguments supplied" vars vals))))

(define (lookup-variable-value var env)
  (define (env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)
             (env-loop (enclosing-environment env)))
            ((eq? var (car vars))
             (car vals))
            (else (scan (cdr vars) (cdr vals)))))
    (if (eq? env the-empty-environment)
        (error "Unbound variable" var)
        (let ((frame (first-frame env)))
          (scan (frame-variables frame)
                (frame-values frame)))))
  (env-loop env))
		  
(define (set-variable-value! var val env)
  (define (env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)
             (env-loop (enclosing-environment env)))
            ((eq? var (car vars))
             (set-car! vals val))
            (else (scan (cdr vars) (cdr vals)))))
    (if (eq? env the-empty-environment)
        (error "Unbound variable -- SET!" var)
        (let ((frame (first-frame env)))
          (scan (frame-variables frame)
                (frame-values frame)))))
  (env-loop env))
  
(define (define-variable! var val env)
  (let ((frame (first-frame env)))
    (define (scan vars vals)
      (cond ((null? vars)
             (add-binding-to-frame! var val frame))
            ((eq? var (car vars))
             (set-car! vals val))
            (else (scan (cdr vars) (cdr vals)))))
    (scan (frame-variables frame)
          (frame-values frame))))  
  

  
(define (setup-environment)
  (let ((initial-env
         (extend-environment (primitive-procedure-names)
                             (primitive-procedure-objects)
                             the-empty-environment)))
    (define-variable! 'true #t initial-env)
    (define-variable! 'false #f initial-env)
    initial-env))  

;;;; 注册基本过程, 并提供调用接口	
(define (primitive-procedure? proc)
  (tagged-list? proc 'primitive))

(define (primitive-implementation proc) (cadr proc))
	
(define primitive-procedures
  (list (list 'car car)
        (list 'cdr cdr)
        (list 'cons cons)
        (list 'null? null?)
		(list 'list? list?)
		(list '+ +)
		(list '- -)
		(list '* *)
		(list '/ /)
		(list '< <)
		(list '> >)
		(list 'eq? eq?)
        ))
(define (primitive-procedure-names)
  (map car
       primitive-procedures))
;;;; ((primitive #[car]) (primitive #[cdr]) (primitive #[cons]) (primitive #[null?]))
(define (primitive-procedure-objects)
  (map (lambda (proc) (list 'primitive (cadr proc)))
       primitive-procedures))
	   
(define apply-in-underlying-scheme apply)
;;;; (apply + '(1 2 3))	   
(define (apply-primitive-procedure proc args)
  (apply-in-underlying-scheme
   (primitive-implementation proc) args))
  
  
;;;; 驱动循环
(define input-prompt ";;; M-Eval input:")
(define output-prompt ";;; M-Eval value:")

(define (driver-loop)
  (prompt-for-input input-prompt)
  (let ((input (read)))
    (let ((output (_eval_ input global-env)))
      (announce-output output-prompt)
      (user-print output)))
  (driver-loop))
  
(define (prompt-for-input string)
  (newline) (display string) (newline))
(define (announce-output string)
  (newline) (display string) (newline))
  
(define (user-print object)
  (if (compound-procedure? object)
      (display (list 'compound-procedure
                     (procedure-parameters object)
                     (procedure-body object)
                     '<procedure-env>))
      (display object)))

;;;; 初始化全局环境
(define global-env (setup-environment))
;;;; 启动该驱动循环
(driver-loop)

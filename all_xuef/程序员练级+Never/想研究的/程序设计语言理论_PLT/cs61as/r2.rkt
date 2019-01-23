#lang racket

(define env0 '())
(define (ext-env x v env)
    (cons `(,x . ,v) env))
;; 查找。在环境中 env 中查找 x 的值。如果没找到就返回 #f
(define (lookup x env)
    (let ([p (assq x env)])
      (cond [(not p) #f]
            [else (cdr p)])))
;; 闭包的数据结构定义,包含一个函数定义 exp 和它定义时所在的环境
(struct Closure (exp env))
(define (interp exp env)
  (match exp
    [(? number? n) n]                                ;数字
    [(? symbol? x)                                   ;变量
       (let ([v (lookup x env)])
         (cond [(not v) (error "undefined variable" x)]
               [else v]))]
    [`(lambda (,x) ,b) (Closure exp env)]            ;函数定义
    [`(let ([,x ,e1]) ,e2)                           ;绑定
       (let ([v1 (interp e1 env)])
         (interp e2 (ext-env x v1 env)))]
    [`(,e1 ,e2)                                      ; 调用
       (let ([v1 (interp e1 env)]
             [v2 (interp e2 env)])
         (match v1
           [(Closure `(lambda (,x) ,e) env-save)
            (interp e (ext-env x v2 env-save))]))]
    [`(,op ,e1 ,e2)                                  ;算术表达式
       (let ([v1 (interp e1 env)]
             [v2 (interp e2 env)])
         (match op
           ['+ (+ v1 v2)]
           ['- (- v1 v2)]
           ['* (* v1 v2)]
           ['/ (/ v1 v2)]))]))

(define (r2 exp)
    (interp exp env0))
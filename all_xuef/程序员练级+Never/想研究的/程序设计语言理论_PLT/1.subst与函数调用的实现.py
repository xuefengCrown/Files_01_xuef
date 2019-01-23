

##过程调用的两种实现思路

"""
f = (lambda (x) (+ x 1)) 为例
(f 2)

1. 使用 (x 2) 扩展外层环境(env)-->new_env, 然后在 new_env中求值函数体(body)

2. 用 2替换掉 函数体中的所有 x, 然后直接求值函数体

问题: 加入过程调用是 (f (+ 1 1)), 我们是用 (+ 1 1)来替换x, 还是用2来替换?

Lazy Evaluation of Eager Evaluation ???

;subst* 与过程调用实现
(define (subst* new old l)
  (cond 
    ((null? l) '())
    ((atom? (car l)) 
      (if (eq? old (car l)) 
          (cons new (subst* new old (cdr l)))
          (cons (car l) (subst* new old (cdr l)))))
    (else (cons (subst* new old (car l)) (subst* new old (cdr l)))))
)
;(subst* 1 'x '(f x (f x (f x x))))

"""

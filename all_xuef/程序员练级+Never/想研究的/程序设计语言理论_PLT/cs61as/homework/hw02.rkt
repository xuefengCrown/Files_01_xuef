#lang racket

(define (squares lst)
  (cond [(null? lst) '()]
        [else (cons (* (car lst) (car lst)) (squares (cdr lst)))]
        ))

;hw02
;;exer3
;;;;((g) 1)-->3
(define (g)
  (lambda (x) (+ 2 x)))

;;exer09
(define (my-every proc l)
  (cond [(null? l) '()]
        [else (cons (proc (car l)) (my-every proc (cdr l)))]
        ))
(define (sq x) (* x x))

;hw04
;;exer02
(define (subst l old new)
  (cond [(null? l) '()]
        [(list? (car l)) (cons (subst (car l) old new) (subst (cdr l) old new))]
        [else (if (equal? old (car l))
                  (cons new (subst (cdr l) old new))
                  (cons (car l) (subst (cdr l) old new))
                  )]
    ))

;;exer04
(define (rv l)
  (cond [(null? l) '()]
        [else (append (rv (cdr l)) (list (car l)))]
    ))

;hw05
;;exer2
(define (sq-tree l)
  (cond [(null? l) '()]
        [(list? (car l))
         (cons (sq-tree (car l)) (sq-tree (cdr l)))]
        [else (cons (* (car l) (car l)) (sq-tree (cdr l)))]
    ))

(define (tree-map proc)
  (lambda (l)
    (cond [(null? l) '()]
        [(list? (car l))
         (cons ((tree-map proc) (car l)) ((tree-map proc) (cdr l)))]
        [else (cons (proc (car l)) ((tree-map proc) (cdr l)))]
    )))

(define sq-t2 (tree-map sq))
;;(sq-t2 (list 1 (list 2 (list 3 4) 5) (list 6 7)))


;;exer7
(define (my-equal? l1 l2)
  (cond [(and (null? l1) (null? l2)) #t]
        [(or (null? l1) (null? l2)) #f]
        [(and (list? (car l1)) (list? (car l2)))
         (and (my-equal? (car l1) (car l2)) (my-equal? (cdr l1) (cdr l2)))]
        [(and (not (list? (car l1))) (not (list? (car l2))))
         (and (eq? (car l1) (car l2)) (my-equal? (cdr l1) (cdr l2)))]
        [else #f]
    ))

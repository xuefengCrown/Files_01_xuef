
# 数据的过程性表示，引发我关于"什么是obj"的哲学思考!

## 一个object可以看作能响应我发出的指令(message)的东西
"""
(define (make-square side)
    (lambda (message)
        (cond ((eq? message 'area)
               (* side side))
              ((eq? message 'perimeter)
               (* 4 side))
              ((EQ? MESSAGE 'TYPE) 'SQUARE)
              (else (error "Unknown message")))))

(define (make-circle radius)
    (lambda (message)
        (cond ((eq? message 'area)
               (* pi radius radius))
              ((eq? message 'perimeter)
               (* 2 pi radius))
              ((EQ? MESSAGE 'TYPE) 'SQUARE)
              (else (error "Unknown message")))))

(define square5 (make-square 5))

(define circle3 (make-circle 3))
"""

#什么是对象以及Why is Message Passing Important?
##it's one of the key ideas in creating object-oriented programming.
##Message passing becomes much more powerful when combined with
##the idea of local state that we'll learn


















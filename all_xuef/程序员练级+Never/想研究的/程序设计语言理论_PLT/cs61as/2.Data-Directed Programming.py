

"""
(define pi 3.141592654)

;;this is the tagged-data version where types are processed
;;by the generic procedure being called
(define (make-square side)
    (attach-tag 'square side))

;;this is the tagged-data version where types are processed
;;by the generic procedure being called
(define (make-circle radius)
    (attach-tag 'circle radius))


;;this is the data-directed version where types and operations 
;;are handled by a data structure that stores the information
(put 'square 'area (lambda (s) (* s s)))
(put 'circle 'area (lambda (r) (* pi r r)))
(put 'square 'perimeter (lambda (s) (* 4 s)))
(put 'circle 'perimeter (lambda (r) (* 2 pi r)))

;;this is the data-directed version where types and operations 
;;are handled by a data structure that stores the information    
(define (area shape-obj)
    (operate 'area shape-obj))

(define (perimeter shape-obj)
    (operate 'perimeter shape-obj))

(define (operate op obj)
    (let ((proc (get (type-tag obj) op)))
      (if proc
          (proc (contents obj))
          (error "Unknown operator for type"))))
          

    
"""

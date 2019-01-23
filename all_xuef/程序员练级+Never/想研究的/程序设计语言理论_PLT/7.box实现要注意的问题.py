
#1
"""
(+ (let ([b (box 0)])
     1)
   b)
   
It should be evident that this program has an error: b in the right branch of
the addition is unbound.

"""

#2
"""
#lang plai

(let ([a (box 1)])
  (let ([f (lambda (x) (+ x (unbox a)))])
    (begin
      (set-box! a 2)
      (f 10))))

-->12
"""

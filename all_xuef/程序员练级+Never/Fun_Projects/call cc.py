
#call/cc 接受一个函数，该函数接受一个参数，此参数即为 current continuation。

#k表示后续(continuation)
##以 (+ (* 3 4) 5) 为例
"""
(+ (* 3 4) 5)   k: (λ (v) v)
(* 3 4)         k: (λ (v) (+ v 5))
3               k: (λ (v) (+ (* v 4) 5))
"""

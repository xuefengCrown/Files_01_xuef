
# 《The Little Schemer》 p135
"""
Is rel a fun
where rel is  ((4 3) (4 2) (7 6) (6 2) (3 4))

(firsts rel) 表示定义域
(seconds rel) 表示值域

(define (fun? rel)
  (set? (firsts rel)))

"""
# How do we represent a finite function?
"""
For us, a finite function is a list of pairs in
which no first element of any pair is the same
as any other first element.
"""

##Why is #t the value of (fullfun? fun)
##where fun is ((8 3) (4 8) (7 6) (6 2) (3 4))
"""Because (3 8 6 2 4) is a set."""

"""
(define (fullfun? rel)
  (set? (seconds rel)))
"""

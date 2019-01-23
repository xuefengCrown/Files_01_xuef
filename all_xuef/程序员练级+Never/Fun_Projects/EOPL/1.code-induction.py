

##  (nth-element '(a b c d e) 3)
##= (nth-element '(b c d e) 2)
##= (nth-element '(c d e) 1)
##= (nth-element '(d e) 0)
##= d


#> (invert '((a 1) (a 2) (1 b) (2 b)))
## ((1 a) (2 a) (b 1) (b 2))

def invert(lst): # lst is a list of 2-lists (lists of length two)
    for ele in lst:
        e1,e2 = ele
        yield (e2,e1)

lst = (('a', 1), ('a', 2), (1, 'b'), (2, 'b'))
inverted = invert(lst)
for ele in inverted:
    print(ele)

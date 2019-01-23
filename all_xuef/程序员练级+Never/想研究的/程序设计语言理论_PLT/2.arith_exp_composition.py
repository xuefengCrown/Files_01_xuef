
#What are the rules that govern nesting of arithmetic expressions?
#We’re actually free to nest any expression inside another.
"""
NumE
PlusE
MultE

(define-type ArithC
  [numC (n : number)]
  [plusC (l : ArithC) (r : ArithC)]
  [multC (l : ArithC) (r : ArithC)])

"""

#scientific mindset

#reduce 规约
#what kind of value might arithmetic expressions reduce to?


"""
Third, and most subtly, there’s something conceptually wrong about modifying ArithC.
That’s because ArithC represents our core language. In contrast, subtraction and other
additions represent our user-facing, surface language.
"""

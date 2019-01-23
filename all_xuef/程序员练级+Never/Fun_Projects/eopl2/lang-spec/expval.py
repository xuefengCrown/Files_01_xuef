
# the expressed and denoted values
"""
ExpVal = Int + Bool + Proc +  Ref(ExpVal)
DenVal = ExpVal
"""


"""
(newref-exp (exp1)
  (let ((v1 (value-of exp1 env)))
    (ref-val (newref v1))))

(deref-exp (exp1)
  (let ((v1 (value-of exp1 env)))
    (let ((ref1 (expval->ref v1)))
      (deref ref1))))

(setref-exp (exp1 exp2)
  (let ((ref (expval->ref (value-of exp1 env))))
    (let ((val2 (value-of exp2 env)))
      (begin
        (setref! ref val2)
        (num-val 23)))))


In this interpreter, value-of would return both a value and a store, just as in the specification.
A fragment of this interpreter appears in figure 4.6. We call this a store-passing interpreter.
Extend this interpreter to cover all of the language EXPLICIT-REFS.
Everyprocedurethat might modify the storereturns not just its usual value but also a
new store. These are packaged ina data type calledanswer. Complete this definition
of value-of.
"""


#4.5 Parameter-Passing Variations
"""
Call-by-value, in which the denoted value is a reference to a location containing
the expressed value of the actual parameter (section 4.3).
This is the most commonly used form of parameter-passing.
In this section, we explore some alternative parameter-passing mechanisms.
"""

##4.5.1 CALL-BY-REFERENCE
"""
Consider the following expression:
    let p = proc (x) set x = 4
    in let a = 3
       in begin (p a); a end
Under call-by-value, the denoted value associated with x is a reference that
initially contains the same value as the reference associated with a, but these
referencesare distinct. Thus the assignment to x has no effect on the contents
of a’s reference, so the value of the entire expression is 3.

With call-by-value, when a procedure assigns a new value to one of its
parameters,this cannot possibly be seen by its caller.

Though this isolation between the caller and callee is generally desirable,
there are times when it is valuable to allow a procedure to be passed locations
with the expectation that they will be assigned by the procedure.
This may be accomplished by passing the procedure a reference to the location of
the caller’s variable, rather than the contents of the variable.
This parameter-passing mechanism is called call-by-reference.


The only thing that changes is the allocation of new locations.
Under call-by-value, a new location is created for every evaluation of an operand;
under call-by-reference, a new location is created for every evaluation of an
operand other than a variable.
This is easy to implement. The function apply-proceduremust change,
because it is no longer true that a new location is allocated for every proce-
dure call. That responsibility must be moved upstream, to the call-exp
line in value-of, which will have the information to make that decision.
"""
##
"""
We then modify the call-exp line in value-of, and introduce a new
function value-of-operand that makes the necessary decision.
(call-exp (rator rand)
  (let ((proc (expval->proc (value-of rator env)))
        (arg (value-of-operand rand env)))
    (apply-procedure proc arg)))
"""
##value-of-operand
"""
The procedure value-of-operandchecks to see if the operand is a variable.
If it is, then the reference that the variable denotes is returned and then
passed to the procedure by apply-procedure.
Otherwise, the operand is evaluated,and a reference to a new location containing
that value is returned.

value-of-operand : Exp × Env → Ref
(define value-of-operand
  (lambda (exp env)
    (cases expression exp
      (var-exp (var) (apply-env env var))
      (else
        (newref (value-of exp env))))))
        
We could modify let to work in a similar fashion, but we have chosen not to do so,
so that some call-by-valuefunctionality will remain in the language.
More than one call-by-reference parameter may refer to the same location,
as in the following program.
"""
##test code
"""
let b = 3
in let p = proc (x) proc(y)
        begin
          set x = 4;
          y
        end
   in ((p b) b)

This yields 4 since both x and y refer to the same location, which is the binding of b.
This phenomenon is known as variable aliasing. Here x and y are aliases (names) for the same location.
Generally, we do not expect an assignment to one variable to change the value of another,
so aliasing makes it very difficult to understand programs.
"""














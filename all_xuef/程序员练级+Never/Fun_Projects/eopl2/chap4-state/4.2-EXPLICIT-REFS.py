
#4.2 EXPLICIT-REFS: A Language with Explicit References
##store-passing interpreter
##when Locations are created ?
"""
we add references as a new kind of expressed value. So we have
    ExpVal = Int + Bool + Proc + Ref(ExpVal)
    DenVal = ExpVal

We leave the binding structures of the language unchanged, but we add
three new operations to create and use references.
• newref, which allocates a new location and returns a reference to it.
• deref, which dereferences a reference: that is, it returns the contents of
the location that the reference represents.
• setref, which changes the contents of the location that the reference represents.
"""
## write some programs
"""
Below are two procedures, even and odd. They each take an argument,
which they ignore, and return 1 or 0 depending on whether the contents
of the location x is even or odd.
They communicate not by passing data explicitly,
but by changing the contents of the variable they share.

The procedures even and odd do not refer to their arguments;
instead they look at the contents of the location to which x is bound.

In EXPLICIT-REFS, we can store any expressed value, and references are
expressed values. This means we can store a reference in alocation.
"""

##4.2.1 Store-Passing Specifications
"""
In our language, any expression may have an effect. To specify these effects,
we need to describe what store should be used for each evaluation and how
each evaluation can modify the store.

        (value-of exp1 ρ σ0) = (val1 , σ1)
        (value-of exp2 ρ σ1) = (val2 , σ2)
(value-of (diff-exp exp1 exp2) ρ σ0) = (val1 - val2 , σ2)
"""
##xuef: 用 store 来模拟内存?
"""
在 《plai》中，
env:   symbol-->location(just a number, 模拟内存编号-地址)
store: location-->value

"""

##将state表示为global variable
"""
We represent the state of the store as a Scheme value, but we do not explic-
itly pass and return it, as the specification suggests. Instead, we keep the
state in a single global variable, to which all the procedures of the implemen-
tation have access.


"""

##We still have to choose how to model the store as a Scheme value.
"""
We choose the simplest possible model: we represent the store as a list of expressed values,
and a reference is a number that denotes a position in the list.
A new reference is allocated by appending a new value to the list;
and updating the store is modeled by copying over as much of the list as necessary.
"""
##参见 Figure4.1

"""
We add a new variant, ref-val, to the data type for expressed values,
and we modify value-of-program to initialize the store before each evaluation.

value-of-program : Program → ExpVal
(define value-of-program
  (lambda (pgm)
    (initialize-store!)
    (cases program pgm
      (a-program (exp1)
        (value-of exp1 (init-env))))))

Now we can write clauses in value-of for newref, deref, and setref.
The clauses are shown in figure 4.3.
"""























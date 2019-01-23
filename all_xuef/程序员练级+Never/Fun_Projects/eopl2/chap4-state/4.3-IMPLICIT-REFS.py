
#4.3 IMPLICIT-REFS: A Language with Implicit References
##A denoted value is the meaning of a variable.
##An expressed value is the result of an expression. 
"""
Most programming languages take common patterns of allocation, dereferencing,
and mutation, and package them up as part of the language.
Then the programmer need not worry about when to perform these operations,
because they are built into the language.

In this design, every variable denotes a reference.
Denoted values are references to locations that contain expressed values.
References are no longer expressed values. They exist only as the bindings of variables.

    ExpVal = Int + Bool + Proc
    DenVal = Ref(ExpVal)

Locations are created with each binding operation: at each procedure call, let, or letrec.

When a variable appears in an expression, we first look up the identifier in
the environment to find the location to which it is bound, and then we look
up in the store to find the value at that location. Hence we have a “two-level”
system for var-exp.

This design is called call-by-value, or implicit references. Most programming
languages, including Scheme, use some variation on this design.
"""
##set-exp
"""
The contents of a location can be changed by a set expression. We use the syntax
        Expression :: = set Identifier = Expression
                assign-exp (var exp1)
"""
##4.3.1 Specification
"""
We can write the rules for dereference and set easily.
The environment now always binds variables to locations,
so when a variable appears as an expression, we need to dereference it:
    (value-of (var-exp var) ρ σ) = (σ(ρ(var)),σ)
    
reference是一个number，表示内存中的一个location。
dereference是一个动作，它根据location取出相应的内存块中的value。

Assignment works as one might expect: we look up the left-hand side in the environment,
getting a location, we evaluate the right-hand side in the environment,
and we modify the desired location.

We also need to rewrite the rules for procedure call and let to show the
modified store. For procedure call, the rule becomes
    (apply-procedure (procedure var body ρ) val σ)
    = (value-of body [var = l]ρ [l = val]σ)
where l is a location not in the domain of σ.

The rule for (let-exp var exp 1 body) is similar. The right-hand side
exp 1 is evaluated, and the value of the let expression is the value of the
body, evaluated in an environment where the variable var is bound to a new
location containing the value of exp1.
xuef: 求值exp1 可能会modify store!!!
"""
##Exercise 4.14 [*] Write the rule for let.

##现在的environment
"""
env:   symbol-->location(Number)
store: location-->value
"""

##4.3.2 The Implementation
"""
In value-of, we dereference at each var-exp, just like the rules say
    (var-exp (var) (deref (apply-env env var)))

and we write the obvious code for a assign-exp
(assign-exp (var exp1)
  (begin
    (setref!
      (apply-env env var)
      (value-of exp1 env))
  (num-val 27)))

What about creating references? New locations should be allocated at
every new binding. There are exactly four places in the language where new
bindings are created: in the initial environment, in a let, in a procedure call,
and in a letrec.
"""
##p 142












#the environment only grows; it never shrinks.
"""
过程调用时，环境会 grows;
该调用结束然后返回，环境应该 shrinks.(解除绑定)
(或者我们不修改原env，而是返回一个新的扩充后的env?)
但针对下面的情形好像不行!!!

(define (f1 x) (f2 4))
(define (f2 y) (+ x y))
 
(f1 3)

The broken environment interpreter above implements what is known as dynamic scope.
This means the environment accumulates bindings as the program executes.
As a result, whether an identifier is even bound depends on the history of program execution.
We should regard this unambiguously as a flaw of programming language design.
It adversely affects all tools that read and process programs: compilers, IDEs, and humans.

"""


"""
In contrast, substitution—and environments, done correctly—give us lexical scope
or static scope. “Lexical” in this context means “as determined from the source program”,
while “static” in computer science means “without running the program”, so these are
appealing to the same intuition. When we examine an identifier, we want to know two things:
(1) Is it bound? (2) If so, where? By “where” we mean: if there are multiple bindings
for the same name, which one governs this identifier?
"""

# top-level scope
"""
(define y 1)
(define (f x) (+ x y))
(define y 2)
"""
##(f 10) produces 12

#But:
"""
(define y 1)
(define f (let ((z y)) (lambda (x) (+ x y z))))
(define y 2)
"""
##(f 10) produces ? (取决于解释器是怎么实现的)


#Beware
"""
Most “scripting” languages exhibit similar problems. As a result,
on the Web you will find enormous confusion about whether a certain language
is statically- or dynamically-scoped, when in fact readers are comparing behavior
inside functions (often static) against the top-level (usually dynamic). Beware!
"""

#6.5 Exposing the Environment
"""
If we were building the implementation for others to use, it would be wise and a courtesy
for the exported interpreter to take only an expression and list of function definitions,
and invoke our defined interp with the empty environment. This both spares(节省) users an
implementation detail, and avoids the use of an interpreter with an incorrect environment.
In some contexts, however, it can be useful to expose the environment parameter.
For instance, the environment can represent a set of pre-defined bindings: e.g.,
if the language wishes to provide pi automatically bound to 3.2
"""










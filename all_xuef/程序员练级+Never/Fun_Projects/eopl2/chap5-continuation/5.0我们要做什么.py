
#我们要做什么
"""
We will introduce the concept of a continuation as an abstraction of the control context,
and we will write interpreters that take a continuation as an argument,
thus making the control context explicit.
"""
#continuation 作为控制上下文(control context)的抽象
#写一个 以 continuation为参数的解释器

#栈增长的原因
"""
(define fact
  (lambda (n)
    (if (zero? n) 1 ( * n (fact (- n 1))))))

In the recursive definition of factorial,the procedure fact is called in an operand position.
We need to save context around this call because we need to remember that
after the evaluation of the procedure call, we still need to finish evaluating the operands and
executing the outer call, in this case to the waiting multiplication.
"""
#In this chapter we will learn how to track and manipulate control contexts.
"""
Our central tool will be the data type of continuations.
Continuations are an abstraction of the notion of control context, much as environments
are an abstraction of data contexts.
We will explore continuations by writing an interpreter that explicitly passes
a continuation parameter, just as our previous interpreters explicitly passed an
environment parameter.

Once we do this for the simple cases, we can see how to add to our language facilities
that manipulate control contexts in more complicated ways, such as exceptions and threads.
We conclude by showing how these ideas can be applied to a very different programming paradigm,
called logic programming.

"""



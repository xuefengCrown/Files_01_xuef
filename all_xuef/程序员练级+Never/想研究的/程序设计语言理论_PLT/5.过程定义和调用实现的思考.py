
#Scheme design principle?
##Why can’t functions definitions be expressions?
"""
In our current arithmetic-centric language we face the uncomfortable
question “What value does a function definition represent?”,
to which we don’t really have a good answer.
“A function value”

What can we do with functions as values?
Clearly, functions are a distinct kind of value than a number,
so we cannot, for instance, add them.
But there is one evident thing we can do: apply them to arguments!
Thus, we can allow function values to appear in the function position of an application.
The behavior would, naturally, be to apply the function. Thus, we’re proposing a language
where the following would be a valid program (where I’ve used brackets so we can easily
identify the function)

(+ 2 ([define (f x) (* x 3)] 4))

and would evaluate to (+ 2 (* 4 3)), or 14.
"""
##函数定义(function definition)返回什么样的值，决定了它能出现在表达式的什么位置!!!


#7.1 Functions as Expressions and Values
"""
(define-type ExprC
  [numC (n : number)]
  [idC (s : symbol)]
  <app-type>
  [plusC (l : ExprC) (r : ExprC)]
  [multC (l : ExprC) (r : ExprC)]
  <fun-type>)
"""
##We also need to determine what an application looks like.
##What goes in the function position of an application?
##We want to allow an entire function definition, not just its name.

#关于 cs61a-scheme的疑问
"""
过程调用的语法是 (func-name arg)  [func-name : symbol]
如果 (define f (lambda (x) (+ x x)))--> f
那么为什么 ((define f (lambda (x) (+ x x))) 2) 会报 error?
而 ((lambda (x) (+ x x)) 2) 却是正确的? 这不一致!
"""
#So
##What goes in the function position of an application?
##We want to allow an entire function definition, not just its name.

#之前实现的过程调用语法
"""
[appC (fun : symbol) (arg : ExprC)]
"""
##过程定义语法
"""
[fdC (name : symbol) (arg : symbol) (body : ExprC)]
"""

#我们现在要实现的过程调用语法
"""
[appC (fun : ExprC) (arg : ExprC)]
"""
##With this definition of application, we no longer have to look up functions by name,
##so the interpreter can get rid of the list of function definitions.


#1.We need to add a case to the interpreter for function definitions,
#  and this is a good candidate:
"""
[fdC (n a b) expr]
"""

#What happens when you add this?
##Immediately, we see that we have a problem: the interpreter no longer always
##returns numbers, so we have a type error.
"""
(define-type Value
  [numV (n : number)]
  [funV (name : symbol) (arg : symbol) (body : ExprC)])
"""


#A function definition is itself an expression.
#That means a function definition can contain a...function definition.



#A function value needs to remember the substitutions that have already been applied to it.
#Because we’re representing substitutions using an environment, a function value therefore
#needs to be bundled with an environment. This resulting data structure is called a closure.


#闭包
#When encountering a function definition, the interpreter must now remember to save
#the substitutions that have been applied so far




##替换可能的问题
"""
(lambda (f)
  (lambda (x)
    (f 10)))

Now suppose we substitute for f the following expression: (lambda (y) (+ x y))

(lambda (x)
  ((lambda (y) (+ x y)) 10))
But observe that this latter program has no free identifiers!
"""
#we need to define capture-free substitution. It works roughly as follows:
##we first consistently rename all bound identifiers to entirely previously
##unused (known as fresh) names.



#7.5 Sugaring Over Anonymity
"""
(define double (lambda (x) (+ x x)))
(double 10)


((lambda (double)
   (double 10))
 (lambda (x) (+ x x)))


It is so useful that in Racket, it has its own special syntax:
(let ([double (lambda (x) (+ x x))])
  (double 10))
where let can be defined by desugaring as shown above.
"""
#let是语法糖


"""
Here’s a more complex example:
(define (double x) (+ x x))
(define (quadruple x) (double (double x)))
(quadruple 10)

This could be rewritten as
(let ([double (lambda (x) (+ x x))])
  (let ([quadruple (lambda (x) (double (double x)))])
    (quadruple 10)))


but if we change the order, it no longer works—
(let ([quadruple (lambda (x) (double (double x)))])
  (let ([double (lambda (x) (+ x x))])
    (quadruple 10)))
—because quadruple can’t “see” double. so we see that top-level binding is
different from local binding: essentially, the top-level has an “infinite scope”.
This is the source of both its power and problems.
"""

#匿名函数如何实现递归调用???
























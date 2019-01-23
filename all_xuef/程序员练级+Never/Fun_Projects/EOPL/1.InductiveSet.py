##Inductive Set
###嵌套结构与递归
##Because the syntax of a program in a language is usually a nested or tree-like structure,
##recursion will be at the core of our techniques.
##
##当书写一个过程时，我们必须精确描述: 参数是什么?返回值是什么?
##使用归纳法来描述数据集是一个强力方法。
########
##Definition 1.1.1 A natural number n is in S if and only if
##1. n = 0, or
##2. n − 3 ∈ S.
########

##Definition 1.1.3 (list of integers, top-down) A Scheme list is a list of integers
##if and only if either
##1. it is the empty list, or
##2. it is a pair whose car is an integer and whose cdr is a list of integers.

Definition 1.1.4 (list of integers, bottom-up) The set List-of-Int is the smallest
set of Scheme lists satisfying the following two properties:
1. () ∈ List-of-Int, and
2. if n ∈ Int and l ∈ List-of-Int, then (n . l) ∈ List-of-Int.

#Here we use the infix “.” to denote the result of the cons operation in Scheme.


# 语法
For example, we can define the set List-of-Int by the grammar
    List-of-Int :: = ()
    List-of-Int :: = (Int . List-of-Int)
#非终结符 && 终结符
#Productions. The rules are called productions.
Each production has a left-hand side, which is a nonterminal symbol,
and a right-hand side, which consists of terminal and nonterminal symbols
#the symbol :: = , read is or can be.


#推导
List-of-Int
⇒ (Int . List-of-Int)
⇒ (14 . List-of-Int)
⇒ (14 . ())


####几种很有用的集合的定义
#1. s-list
Definition 1.1.6 (s-list, s-exp)
    S-list :: = ( { S-exp } ∗ )
    S-exp :: = Symbol | S-list
#An s-list is a list of s-exps, and an s-exp is either an s-list or a symbol.
##Here are some s-lists.
(a b c)
(an (((s-list)) (with () lots) ((of) nesting)))


#2. binary tree
Definition 1.1.7 (binary tree)
    Bintree :: = Int | (Symbol Bintree Bintree)
##Here are some examples of such trees:
1
2
(foo 1 2)
(bar 1 (foo 1 2))

(baz
    (bar 1 (foo 1 2))
    (biz 4 5))



#3. The lambda calculus
## is a simple language that is often used to study the theory of programming languages.
Definition 1.1.8 (lambda expression)
    LcExp :: = Identifier
          :: = (lambda (Identifier) LcExp)
          :: = (LcExp LcExp)
#where an identifier is any symbol other than lambda.

To see how this works, consider the lambda calculus extended with arithmetic operators. In that language,
    (lambda (x) (+ x 5))
is an expression in which x is the bound variable. This expression describes a procedure that adds 5 to its argument.

Therefore, in ((lambda (x) (+ x 5)) (- x 7))
the last occurrence of x does not refer to the x that is bound in the lambda expression.


# context-sensitive constraint (如 Binary-Search-Tree)
Context-sensitive constraints also arise when specifying the syntax of programming languages.
For instance, in many languages every variable must be declared before it is used.
This constraint on the use of variables is sensitive to the context of their use.
Formal methods can be used to specify context-sensitive constraints,
but these methods are far more complicated than the ones we consider in this chapter.
In practice, the usual approach is first to specify a context-free grammar.
Context-sensitive constraints are then added using other methods.
We show an example of such techniques in chapter 7.


#递归程序，一定存在一个分解问题规模的过程(-->base case)
##until eventually it is called with a problem that can be solved directly, without another call to itself.








































































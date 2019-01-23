
#定义我们的解释器的语法
#以及语义

##1. let


##2. procedure
"""
Expression ::= proc (Identifier) Expression
                    proc-exp (var body)
Expression ::= (Expression Expression)
                    call-exp (rator rand)

let f = proc (x) -(x,11)
in (f (f 77))
"""
##xuef
"""
～如何支持procedure
过程支持包括两方面: 定义和调用
1. 确定语法（syntax）
2. 我们需要一种结构来表示这两种表达式
proc-exp call-exp
3.0 要定义一种类型来表示proc
(define-datatype proc proc?
  (procedure
   (var identifier?)
   (body expression?)
   (saved-env Env?)))
3. 函数定义要返回一个值，要定义proc-val
(var body saved-env)
4. 语义。
在interp中添加对两种表达式(已经结构化为ast)的处理。
"""
##procedure definition要返回什么?
"""
(value-of (proc-exp var body) ρ)
= (proc-val (procedure var body ρ))
"""



#??
"""
记住，Haskell 是一门以表达式为主导（expression-oriented）的语言。
在命令式语言中，代码由陈述（statement）而不是表达式组成，因此在省略 if 语句的 else 分支的情况下，
程序仍是有意义的。但是，当代码由表达式组成时，一个缺少 else 分支的 if 语句，在条件部分为 False 时，
是没有办法给出一个结果的，当然这个 else 分支也不会有任何类型，因此，省略 else 分支对于 Haskell
是无意义的，编译器也不会允许这么做。
"""

"""
-- file: ch02/myDrop.hs
myDrop n xs = if n <= 0 || null xs
              then xs
              else myDrop (n - 1) (tail xs)
"""
#我们将跟在 then 和 else 之后的表达式称为“分支”。不同分支之间的类型必须相同。

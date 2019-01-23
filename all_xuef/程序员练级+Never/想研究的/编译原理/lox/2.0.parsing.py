
#Formal_grammer
#关键词：AST, CFG, Tree
##抽象语法树，上下文无关文法， 树
"""
Along the way, we’ll cover some theory around formal grammars,
feel the difference between functional and object-oriented programming,
go over a couple of design patterns, and do some metaprogramming.

"""

#a representation for code.
"""
Before we do all that, let’s focus on the main goal—a representation for code.

It should be simple for the parser to produce and easy for the interpreter to consume.

a workable representation of our code is a tree that matches the
grammatical structure of the language.
"""

##求值与后序遍历
"""
In order to evaluate an arithmetic node, you need to know the numeric values of its subtrees,
so you have to evaluate those first. That means working your way from the leaves up to
the root—a post-order traversal.
"""

##CFG
"""
But regular languages aren’t powerful enough to handle expressions which can nest
arbitrarily deeply.
"""

##lox
"""
expression → literal
           | unary
           | binary
           | grouping ;

literal    → NUMBER | STRING | "true" | "false" | "nil" ;
grouping   → "(" expression ")" ;
unary      → ( "-" | "!" ) expression ;
binary     → expression operator expression ;
operator   → "==" | "!=" | "<" | "<=" | ">" | ">="
           | "+"  | "-"  | "*" | "/" ;

This grammar is actually ambiguous, which we’ll see when we get to parsing it.
But it’s good enough for now.
"""

##Metaprogramming the trees

##Working with Trees
"""
Put on your imagination hat for a moment. Even though we aren’t there yet,
consider what the interpreter will do with the syntax trees.
"""

##优先级与结合性来消除表达式的歧义
##注意，scheme中没有这种歧义，所以不需要优先级和结合性
"""
5 - 3 - 1
is equivalent to: (5 - 3) - 1  (左结合)

a = b = c
is equivalent to: a = (b = c)  (赋值语句是右结合的)

Without well-defined precedence and associativity, an expression that uses multiple operators
is ambiguous—it can be parsed into different syntax trees, which could in turn evaluate to
different results.
"""

#可以将优先级和结合性 编码进 CFG中









           




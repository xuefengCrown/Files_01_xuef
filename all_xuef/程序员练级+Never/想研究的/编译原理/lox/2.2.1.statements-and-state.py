
#Statements and State

##bind a name to some data or function.
##To support bindings, our interpreter needs internal state.
##So in this chapter, we will give our interpreter a brain that can not just process, but remember.
"""
We’ll define statements that produce output (print) and create state (var).
We’ll add expressions to access and assign to variables.
Finally, we’ll add blocks and local scope.
"""

##扩展语法
"""
Since Lox is an imperative, dynamically-typed language, the “top level” of a script is
simply a list of statements. The new rules are:

program   → statement* EOF ;

statement → exprStmt
          | printStmt ;

exprStmt  → expression ";" ;
printStmt → "print" expression ";" ;
"""

##what's a program? ::= a list of statements

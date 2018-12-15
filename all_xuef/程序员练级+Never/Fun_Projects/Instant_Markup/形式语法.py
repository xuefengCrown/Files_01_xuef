
#Three Models for the Description of Language
"""
Regular languages
context-free
context-sensitive
recursively enumerable
"""
##Type 3 languages are called regular languages. Anything you can match with a regular expression
##is perfect example of a regular language — hence the name “regular” expression.
##Any regular language can be solved with a deterministic finite automata (DFA).
##
##For those less familiar, a DFA is a program that can be represented as a fixed set of
##states (nodes) and transitions (edges).


#Type 2 — Context-Free languages
##can be represented as a pushdown automata which is an automata that can maintain
##some state with a stack.

#This part of the hierarchy gets the most attention because most programming languages
#and domain specific languages are context-free.

##Ambiguity is painful. Markdown is a good example of an ambiguous grammar/

#For unambiguous context-free languages like C, there are all kinds of tools.
#The most popular are ANTLR, Bison, and YACC.



###########################################
#If you’re familiar with functional programming and category theory, you’ll really
#appreciate the elegance of parser combinators.












































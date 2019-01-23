
#inductive def
"""
Given our general goal to define and reason about programming languages,
we will have to deal with a variety of description tasks.

The first is to describe the grammar of a language.
The second is to describe its static semantics, usually via some typing rules.
The third is to describe its dynamic semantics, often via transitions of an abstract machine.
On the surface, these appear like very different formalisms (grammars, typing rules,
abstract machines) but it turns out that they can all be viewed as special
cases of inductive definitions.

"""
##
"""
如何描述一门语言的语法？ 正则表达式 && CFG(上下文无关文法)
如何描述它的 静态语义？(via type rules)
如何描述它的 动态语义？(via evaluation rules)

"""

#As a simple example
"""
we consider the language of properly matched parentheses over the alphabet Σ = {(, )}.
This language can be defined by the grammar
M ::= ε | (M) | M M
with the only non-terminal M. Recall that ε stands for the empty string.
"""

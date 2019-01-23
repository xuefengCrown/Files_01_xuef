
#OVERVIEW
"""
The scanner’s task is to transform a stream of characters into a stream of
words in the input language. Each word must be classified into a syntactic
category, or “part of speech.”
"""

##正则
"""
This chapter introduces regular expressions, a notation used to describe
the valid words in a programming language.
"""
# Keywords: Scanner, Finite Automaton, Regular Expression, Fixed Point

#微语法
"""
to accomplish this aggregation and classification, the scanner applies a set of
rules that describe the lexical structure of the input programming language,
sometimes called its microsyntax.
The microsyntax of a programming language specifies how to group characters into words.

Western languages, such as English, have simple microsyntax. Adjacent
alphabetic letters are grouped together, left to right, to form a word.
A blank space terminates a word, as do most nonalphabetic symbols.  
"""
##关键字
"""
In a typical programming language, some words, called keywords or reserved words,
match the rule for an identifier but have special meanings.

Keyword: a word that is reserved for aparticular syntactic purpose
and,thus,can not be used as an identifier.
"""

#有限自动机

#2.3 REGULAR EXPRESSIONS
"""
The set of words accepted by a finite automaton, F , forms a language, denoted L( F ).
The transition diagram of the fa specifies, in precise detail, that language.

与 FA 等价。
To model more complex constructs, such as integers or identifiers, we need
a notation that can capture the essence of the cyclic edge in an fa.
为对更复杂的结构建模，re中需要一种记法，来捕获 FA中循环边的本质。
"""

##2.3.1 Formalizing the Notation

##2.3.3 Closure Properties of REs


##2.4.1 Nondeterministic Finite Automata
##???

#形式语言和自动机理论





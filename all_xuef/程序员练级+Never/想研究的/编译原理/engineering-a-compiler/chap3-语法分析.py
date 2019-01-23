#Parsers
"""
The parser’s task is to determine if the input program, represented by the
stream of classified words produced by the scanner, is a valid sentence in the
programming language. To do so, the parser attempts to build a derivation
for the input program, using a grammar for the programming language.
"""

## context-free grammars(上下文无关文法)
"""
context-free grammars, a notation used to specify the syntax of programming languages.
It develops several techniques for finding a derivation, given a grammar and an input program.

Keywords: Parsing, Grammar, ll(1), lr(1), Recursive Descent
"""

##如何描述语法?
##符号表示法
"""
RE 缺乏描述语言完整语法的能力。

"""
##3.2.1 Why Not Regular Expressions?
"""
In principle, dfas cannot count. While they work well for microsyntax, they are not suitable to
describe some important programming language features.
"""

##3.2.2 Context-Free Grammars
"""
To describe programming language syntax, we need a more powerful notation
than regular expressions that still leads to efficient recognizers.

Context-free grammar
For a language L,its CFG defines the sets of strings of symbols that are valid sentences in L.

A context-free grammar, G, is a set of rules that describe how to form sentences.
"""

##power of CFG
"""
let’s revisit the example that showed the shortcomings of res:
the language of expressions with parentheses.

This simple cfg for expressions cannot generate a sentence with unbalanced
or improperly nested parentheses.
"""
##二义性???

##3.2.4 Encoding Meaning into Structure
"""

"""

## 语法分析
"""
the parser makes a series of choices about which productions to apply.
Most of the intellectual complexity in parsing lies in the mechanisms for making these choices. 
"""

##如何将语义编码到语法和结构中?



























#编译器流程

|Source Code|----->|Tokens|----->|AST|----->|Decorated AST|
             Lexcical      Parsing    Semantic
             Analysis                 Analysis

##Lexcical Analysis-->Tokens
"""
Token consists of syntactic category (like “noun” or “adjective”) plus
semantic information (like a particular name).

标识符 + 数字常量
For programming, semantic information might be text of identifier or numeral.
"""


#ASTs
"""
• Each type of AST node contains an integer value indicating what
type of node it is.

• Can use these to distinguish node types, and for Project 1, the
default method declarations given in AST suffice for most of the project.

• For later projects, I suggest using a more OOP style, allowing different nodes
to react in different ways without a specific test for node type.

• To this end, we’ve set up a mechanism that allows the NODE and LEAF
choose subtypes of AST for specific node types. See the examples
in stmts.cc and exprs.cc .

• Although you don’t need to do tree-processing in this project, aside
from building them, you may want to handle checks for improper
placement of break , continue , return , def , and class by doing a
recursive post-pass over the tree. Alternative is using some global
variables in the parser.
"""

##xuef: thoughts on oop
##oop，基于实例所属类型的不同将指定动作自动分派到各实例的方法。

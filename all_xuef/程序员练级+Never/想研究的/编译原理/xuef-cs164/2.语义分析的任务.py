
#Typical Tasks of the Semantic Analyzer
"""
• Find the declaration that defines each identifier instance

• Determine the static types of expressions
确定表达式的类型

• Perform re-organizations of the AST that were inconvenient in parser,
or required semantic information
重构 AST，使之更容易操作或为之添加语义信息。

• Detect errors and fix to allow further processing
探测错误，如果需要则修复它。
"""

#Typical Semantic Errors: Java, C++
"""
• Multiple declarations: a variable should be declared (in the same region) at most once

• Undeclared variable: a variable should not be used without being declared.

• Type mismatch: e.g., type of the left-hand side of an assignment
should match the type of the right-hand side.

• Wrong arguments: methods should be called with the right number and types of arguments.

• Definite-assignment check (Java): conservative check that simple
variables assigned to before use.
"""








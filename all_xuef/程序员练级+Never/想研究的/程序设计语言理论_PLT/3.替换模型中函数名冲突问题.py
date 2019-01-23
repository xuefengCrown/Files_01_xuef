
"""
Before we turn this into code, there’s an important case to consider.
Suppose the name we are substituting happens to be the name of a function.
Then what should happen?


There are many ways to approach this question.
One is from a design perspective: function names live in their own “world”,
distinct from ordinary program identifiers. Some languages (such as C and Common Lisp,
in slightly different ways) take this perspective, and partition identifiers into
different namespaces depending on how they are used. In other languages,
there is no such distinction; indeed, we will examine such languages soon.

"""

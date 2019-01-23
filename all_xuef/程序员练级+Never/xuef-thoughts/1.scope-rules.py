
#scope-rules

##一些术语
"""
• Declarative region: section of text or program execution that bounds
scopes of declarations (we’ll say “ region ” for short).
• If scope of a declaration defined entirely according to its position
in source text of a program, we say language is statically scoped.

"""

##Scope Rules: Nesting
"""
choose the one defined in the innermost (most deeply nested) declarative region.

Variations on this: Java disallows attempts to hide local variables and parameters.
"""

##Scope Rules: Declarative Regions
"""
• Languages differ in their definitions of declarative regions.
• In Java, variable declaration’s effect stops at the closing ‘ } ’, that
is, each function body is a declarative region.

• In Python, function header and body make up a declarative region,
as does a lambda expression. But nothing smaller. Just one x in this
program:

"""

def f(x):
    x=3
    L = [x for x in range(10)]
    print(L)

f(2)

##Scope Rules: Use Before Definition
"""
• Languages have taken various decisions on where scopes start.
• In Java, C++, scope of a member (field or method) includes the entire class
(textual uses may precede declaration).
• But scope of a local variable starts at its declaration.
"""

##Scope Rules: Overloading
"""
• In Java or C++ (not Python or C), can use the same name for more than one method,
as long as the number or types of parameters are unique.
    int add(int a, int b); float add(float a, float b);
    
• The declaration applies to the signature —name + argument types—not just name.

• But return type not part of signature, so this won’t work:
    int add (int a, int b); float add (int a, int b)

"""

##Explicit vs. Implicit Declaration
"""
• Java, C++ require explicit declarations of things.
• C is lenient: if you write foo(3) with no declaration of foo in scope, C will supply one.

• Python implicitly declares variables you assign to in a function to be local variables.

• Fortran implicitly declares any variables you use, and gives them a
type depending on their first letter.
• But in all these cases, there is a declaration as far as the compiler is concerned.
"""


#Topic: walk with ast

#http://www.python.org/dev/peps/pep-0339/ -- Design of the CPython Compiler
#https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts

#See also Green Tree Snakes,
"""
an external documentation resource, has good details on working with Python ASTs.

Abstract Syntax Trees, ASTs, are a powerful feature of Python.
You can write programs that inspect and modify Python code,
after the syntax has been parsed, but before it gets compiled to byte code.
That opens up a world of possibilities for introspection,(a reflective looking inward)
testing, and mischief.
"""

##Python 代码编译过程
"""
Starting with Python 2.5, the Python compiler (the part that takes your source-code and
translates it to Python VM code for the VM to execute) works as follows [1]:
1. Parse source code into a parse tree (Parser/pgen.c)
2. Transform parse tree into an Abstract Syntax Tree (Python/ast.c)
3. Transform AST into a Control Flow Graph (Python/compile.c)
4. Emit bytecode based on the Control Flow Graph (Python/compile.c)
"""

##为什么要关心 ast? 利用它我们能做些什么?
"""
1. Reproducing Python source from AST nodes
    Armin Ronacher [5] wrote a module named codegen that uses the facilities of ast
    to print back Python source from an AST. Here's how to show the source for the
    node we transformed in the previous example.

    codegen is very useful for debugging or tools that transform Python code and want to
    save the results [6].

    [6] For example, the pythoscope tool for auto generating unit-tests from code could
    probably benefit from ast and codegen. Currently it seems to be working on the level
    of Python parse trees instead.
"""

##So why is this useful?
"""
Many tools require parsing the source code of the language they operate upon.
With Python, this task has been trivialized by the built-in methods to parse Python source
into convenient ASTs. Since there's very little (if any) type checking done in a Python compiler,
in classical terms we can say that a complete Python front-end is provided.
This can be utilized in:

- IDEs for various "intellisense" needs
IDE 中的"智能提示"
- Static code checking tools like pylint and pychecker
静态代码检查
- Python code generators like pythoscope
- Alternative Python interpreters
- Compilers from Python to other languages

"""


















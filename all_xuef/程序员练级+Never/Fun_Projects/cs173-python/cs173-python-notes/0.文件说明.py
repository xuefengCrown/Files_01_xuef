
#python-syntax.rkt
This contains a (currently tiny) datatype that is intended to be a Racket
representation of Python programs. You are free to change this to suit the
needs of your particular design.

#python-core-syntax.rkt
This contains a (currently tiny) specification for a core language.
We write our interpreter over this data structure.

#python-desugar.rkt
Contains the definition for desugar, a function from Python surface syntax
(from python-syntax.rkt), to core syntax (python-core-syntax.rkt).

#get-structured-python.rkt and parse-python.rkt
These two files work together to parse Python files into the definition given
in python-syntax.rkt. parse-python.rkt uses your system's implementation of Python,
in coordination with python-parser.py, to generate a JSON representation of Python source.
This JSON representation lines up with
the AST specification of Python programs.
#https://docs.python.org/release/3.2.1/library/ast.html
Each dictionary has a "type" field that corresponds to the name of a constructor
in the specification. For example:



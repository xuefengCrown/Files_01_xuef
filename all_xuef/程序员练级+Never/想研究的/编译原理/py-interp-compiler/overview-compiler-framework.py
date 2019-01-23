
#Intermediate Representations 
"""
Front End emits IR for the rest of the compiler to use

·Rest of the compiler works from IR
– Analyzes IR to learn about the code
– Transforms IR to improve final code

·IR determines what a compiler can do to the code
– Can only manipulate details that are represented in the IR


IR is the vehicle that carries information between phases
• Front end: produces an IR version of the input program
• Optimizer: transforms the IR into an equivalent IR that runs faster
– Each “pass” reads and writes IR
• Back end: systematically transforms the IR into native code

IR determines both the compiler’s ambition & its chances for success
• The compiler’s knowledge of the code is encoded in the IR
• The compiler can only manipulate what is represented by the IR
"""

##IR design time
"""
Decisions in IR design affect the speed and efficiency of the compiler
Some important IR properties
• Ease of generation
• Ease of manipulation
• Cost of manipulation
• Procedure size
• Expressiveness
• Level of abstraction
"""

##
"""
Today, we will focus on representing the operations in the code
• Arithmetic expressions
• Assignment
• Control-flow in the program
Later, we will come back and talk about representing names & objects
• Symbol tables
• Renaming
• Storage models
"""

##Three major categories
"""
• Structural IRs
– Graphically oriented
– Heavily used in source-to-source translators
– Tend to be large

Examples:
Trees, DAGs


• Linear IRs
– Pseudo-code for an abstract machine
– Level of abstraction varies
– Simple, compact data structures
– Easier to rearrange

Examples:
3 address code
Stack machine code


• Hybrid IRs
– Combination of graphs and linear code
– Example: control-flow graph

Examples:
Control-flow graph
SSA Form 
"""

##Syntax Tree
"""
Syntax trees are often used in source-tosource systems
• Captures the precise (syntactic) form of the input program

Syntax trees tend to be inefficient
• Lots of unnecessary nodes and edges
• Lots of implicit detail that might be useful to represent explicitly
"""
###Syntax trees can be represented with a linear notation (e.g., prefix or postifx)


##Abstract Syntax Tree
"""
An abstract syntax tree is the procedure’s parse tree with the
nodes for most non-terminal nodes removed.

   -
 /   \
x     *
    /   \
   2     y

• ASTs are space efficient trees that capture most of the interesting
information found in a syntax tree
– Can regenerate source code in a treewalk, with a little cleverness
– Many fewer nodes and edges than in a syntax tree.
• S-expressions in Scheme or Lisp, are (essentially) ASTs
"""

##DAG 有向无环图
"""
A directed acyclic graph (DAG) is an AST with a unique node for each value .

With two copies of the same expression, the compiler may
be able to arrange the code to evaluate it only once.
"""
























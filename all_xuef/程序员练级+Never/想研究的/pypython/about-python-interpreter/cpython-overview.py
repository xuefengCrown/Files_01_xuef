
#vm
"""
Your CPU is just a complex electronic machine which receives all input (machine code, data),
it has a state (registers), and based on the input and its state it will output stuff
(to RAM or a Bus), right?

"""


#PyEval_EvalFrameEx
"""
PyEval_EvalFrameEx implements CPython’s evaluation loop, which is to say that
it’s a function that takes a frame object and iterates over each of the opcodes
in its associated code object, evaluating (interpreting, executing) each opcode
within the context of the given frame
(this context is chiefly the associated namespaces and interpreter/thread states).
"""

#vm是个字节码解释器

##字节码组成
"""
This opcode (and many others) works with values on the value stack as well as with
a few temporary variables.

Next, we see a very simple opcode that loads values from somewhere into the valuestack.
I chose to quote LOAD_CONST because it’s very brief and simple, although it’s not really
a namespace related opcode. “Real” namespace opcodes load values into the value stack
from a namespace and store values from the value stack into a namespace;

"""

##各种初始化？


##namespace
"""
the names are “loaded” from the globals and locals namespaces
"""

##
"""
each Python thread is represented by its own thread state, which (among other things)
points to the stack of currently executing frames. After the frame object is created
and placed at the top of the thread state stack, it (or rather, the byte code pointed by it)
is evaluated, opcode by opcode, by means of the (rather lengthy)
"""

##eval
"""
PyEval_EvalFrameEx takes the frame, extracts opcode (and operands, if any, we’ll get to that)
after opcode, and executes a short piece of C code matching the opcode.
"""












#https://docs.python.org/3/reference/executionmodel.html
"""
A Python program is constructed from code blocks. A block is a piece of
Python program text that is executed as a unit.

The following are blocks: a module, a function body, and a class definition.
Each command typed interactively is a block.
A script file (a file given as standard input to the interpreter or specified
as a command line argument to the interpreter) is a code block.
A script command (a command specified on the interpreter command line with the ‘-c’ option)
is a code block. The string argument passed to the built-in functions eval()
and exec() is a code block.

"""

##code obj
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

"""
    co_argcount = 1
    co_cellvars = ()
    co_code = b'|\x00d\x01\x16\x00d\x02k\x02r\x1e|\x00d\x03\x16\x00d\x02k\x02r\x1ed\\
x04S\x00n,|\x00d\x01\x16\x00d\x02k\x02r0d\x05S\x00n\x1a|\x00d\x03\x16\x00d\x02k\x02r\
Bd\x06S\x00n\x08t\x00|\x00\x83\x01S\x00d\x00S\x00'
    co_consts = (None, 3, 0, 5, 'FizzBuzz', 'Fizz', 'Buzz')
    co_filename = /Users/c4obi/projects/python_source/cpython/fizzbuzz.py
    co_firstlineno = 6
    co_flags = 67
    co_freevars = ()
    co_kwonlyargcount = 0
    co_lnotab = b'\x00\x01\x18\x01\x06\x01\x0c\x01\x06\x01\x0c\x01\x06\x02'
    co_name = fizzbuzz
    co_names = ('str',)
    co_nlocals = 1
    co_stacksize = 2
    co_varnames = ('n',)
"""
#Each of these bytecode instruction sequence is composed of an opcode and
#an oparg - argument to the opcode where it exists.
#co_varnames references the locally defined names while
#co_names references non-locally defined names.
#co_stacksize value is the maximum number of items that exist on the evaluation stack
##at any point during the execution of the code block.

#co_freevars: The co_freevars field is a collection of free variables defined
#within the code block. This field is mostly relevant to nested functions that form closures.

#Special cell objects are created for storing values in this cell variable collection
#during the execution of the code object.


#The bytecode - co_code in more detail.

"""
Bytecode instructions are two bytes in size - one byte for the opcode and
the second byte for the argument to the opcode. In the case where the opcode
does not take an argument then the second argument byte is zeroed out.

Sometimes, the argument to an opcode maybe unable to fit into the default single byte.
For these kind of arguments, the python virtual machine makes use of the EXTENDED_ARG opcode.

"""


##Frame
"""
6. Frames Objects
Code objects contain the executable byte code but lack the contextual information
required for the execution of such code.

One can think of the frame object as a container in which the code object is
executed - it knows about the code object and has references to data and values that
are required during the execution of some code object.

Before a code object can be executed, a frame object within which the execution of
such a code object takes place has to be created. Such a frame object contains all
the namespaces required for execution of a code object (local, global, and builtin),
a reference to the current thread of execution, stacks for evaluating byte code and
other housekeeping information that are important for executing byte code.

typedef struct _frame {
        PyObject_VAR_HEAD
        struct _frame *f_back;      /* previous frame, or NULL */
        PyCodeObject *f_code;       /* code segment */
        PyObject *f_builtins;       /* builtin symbol table (PyDictObject) */
        PyObject *f_globals;        /* global symbol table (PyDictObject) */
        PyObject *f_locals;         /* local symbol table (any mapping) */
        PyObject **f_valuestack;    /* points after the last local */
        PyObject **f_stacktop;
        PyObject *f_trace;          /* Trace function */

        /* fields for handling generators*/
        PyObject *f_exc_type, *f_exc_value, *f_exc_traceback;
        /* Borrowed reference to a generator, or NULL */
        PyObject *f_gen;

        int f_lasti;                /* Last instruction if called */
        int f_lineno;               /* Current line number */
        int f_iblock;               /* index in f_blockstack */
        char f_executing;           /* whether the frame is still executing */
        PyTryBlock f_blockstack[CO_MAXBLOCKS]; /* for try and loop blocks */
        PyObject *f_localsplus[1];  /* locals+stack, dynamically sized */
    } PyFrameObject;

f_back: This field is a reference to the frame of the code object that was executing prior to the current code object. Given a set of frame objects, the f_back fields of these frames together form a stack of frames that goes all the way back to the initial frame. This initial frame then has a NULL value in this f_back field. This implicit stack of frames forms what we refer to as the call stack.
f_code: This field is a reference to a code object. This code object contains the bytecode that is executed within the context of this frame.
f_builtins: This is a reference to the builtin namespace. This namespace contains names such as print, enumerate etc and their corresponding values.
f_globals: This is a reference to the global namespace of a code object.
f_locals: This is a reference to the local namespace of a code object. As previously mentioned these names have been defined within the scope of a function. When we discuss the f_localplus field, we will see an optimization that python does when working with locally defined names.
f_valuestack: This is a reference to the evaluation stack for the frame. Recall that the python virtual machine is a stack-based virtual machine so during evaluation of bytecode, values are read from the top of a stack and results from the evaluation of byte code are stored on the top of a stack. This field is the stack that is used during code object execution. The stacksize of a frame’s code object gives the maximum depth to which this data structure can grow to.
f_stacktop: As the name suggests, the field points to the next free slot of the evaluation value stack. When a frame is newly created, this value is set to the value stack - this is the first available space on the stack as there are no items on the stack.
f_trace: This field references a function that is used for tracing the execution of python code.
f_exc_type, f_exc_value, f_exc_traceback, f_gen: are fields that are used for book keeping in order to be able to cleanly execute generator code. More on this when we discuss python generators.
f_localplus: This is a reference to an array that contains enough space for storing cell and local variables. This field provides a mechanism for the evaluation loop to optimize loading and storing values of names to and from the value stack with the LOAD_FAST and STORE_FAST instructions. The LOAD_FAST and STORE_FAST opcodes provides faster name access than their counterpart LOAD_NAME and STORE_NAME opcodes because they use array indexing for accessing value of names and this is done in approximately constant time unlike their counterparts that search a mapping for the value associated with a given name. When we discuss the evaluation loop, we see how this value is set up during the frame bootstrapping process.
f_blockstack: This field references a data structure that acts as a stack which is used to handle loops and exception handling. This is the second stack in addition to the value stack that is of utmost importance to the virtual machine but this does not receive as much attention as it rightfully should. The relationship between the block stack, exceptions and looping constructs is quite complex and we look at that in the coming chapters

"""











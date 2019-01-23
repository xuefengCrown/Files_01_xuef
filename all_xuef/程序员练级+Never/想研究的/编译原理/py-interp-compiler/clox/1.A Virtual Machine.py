
##why vm
"""
We know what instructions are in theory, but we’ve never seen them living and breathing,
so it’s hard to really understand what they do. It would be hard to write a compiler that
outputs bytecode when we don’t have a good understanding of how that bytecode behaves.
"""

##An Instruction Execution Machine
"""
The “virtual machine” is one part of our interpreter’s internal architecture.
You hand it a chunk of code—literally a Chunk—and it runs it.

typedef struct {  
  Chunk* chunk;   
} VM;             

void initVM();    
void freeVM();


As usual, we start simple. The VM will gradually acquire a whole pile of state
it needs to keep track of, so we define a struct now to stuff that all in.
Currently, all we store is the chunk that it executes.

"""
#xuef:虚拟机只是内存中的一片结构化数据而已，是 CPU 赋予它生命。

##Executing instructions
"""
The READ_BYTE macro reads the byte currently pointed at by ip and then advances the
instruction pointer. The first byte of any instruction is the opcode.

Given a numeric opcode, we need to get to the right C code that implements that
instruction’s semantics. This process is called “decoding” or “dispatching”
the instruction.

we have a single giant switch statement with a case for each opcode.
The body of each case implements that opcode’s behavior.

"""

##A Value Stack Manipulator
"""
In addition to imperative side effects, Lox has expressions that produce,
modify, and consume values. Thus, our compiled bytecode needs a way to
shuttle( frequently go from one place to the other) values
around between the different instructions that need them.
"""
###post-order traversal on ast
"""
Our old jlox interpreter accomplishes this by recursively traversing the AST.
It does a post-order traversal. First it recurses down the left operand branch,
then the right operand, then finally it evaluates the node itself.

后序遍历的本质就是 根问题的答案依赖于诸个子问题的解决。
"""
###中间值存储在何处？
"""
After evaluating the left operand, jlox needs to store that result somewhere
temporarily while it’s busy traversing down through the right operand tree.
We used a local variable in Java for that. Our recursive tree-walk interpreter
creates a unique Java call frame for each node being evaluated, so we could have
as many of these local variables as we needed.

In clox, our run() function is not recursive—the nested expression tree is flattened out
into a linear series of instructions.
We don’t have the luxury of using C local variables, so how and where should we store
these temporary values?
"""
###but we rarely learn why computers are architected this way.

##The VM’s Stack


##An Arithmetic Calculator
"""
The heart and soul of our VM are in place now.
The bytecode loop dispatches and executes instructions.
The stack grows and shrinks as values flow through it.

Get a feel for how cleverly they interact.
"""






























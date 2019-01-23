
#Frames
"""
A frame is a collection of information and context for a chunk of code.

Frames are created and destroyed on the fly as your Python code executes.
There's one frame corresponding to each call of a function—so while each frame
has one code object associated with it, a code object can have many frames.

If you had a function that called itself recursively ten times, you'd have
eleven frames—one for each level of recursion and one for the module you started from.

In general, there's a frame for each scope in a Python program.

For example, each module, each function call, and each class definition has a frame.

Frames 动态创建与销毁。

"""

##RETURN_VALUE
"""
字节码指令RETURN_VALUE告诉解释器在frame间传递一个值。
首先，它把位于调用栈栈顶的frame中的数据栈的栈顶值弹出。然后把整个frame弹出丢弃。
最后把这个值压到下一个frame的数据栈中。


回头在看看这个bug，我惊讶的发现Python真的很少依赖于每个frame有一个数据栈这个特性。
在Python中几乎所有的操作都会清空数据栈，所以所有的frame公用一个数据栈是没问题的。
在上面的例子中，当bar执行完后，它的数据栈为空。即使foo公用这一个栈，它的值也不会受影响。
然而，对应生成器，一个关键的特点是它能暂停一个frame的执行，返回到其他的frame，一段时间后
它能返回到原来的frame，并以它离开时的同样的状态继续执行。
"""

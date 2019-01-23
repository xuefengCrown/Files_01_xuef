
#cps转换与尾递归优化
"""
In a later chapter, I'll show how the mechanisms that support tail recursion also support
a powerful control feature called call-with-current-continuation that lets you implement
novel control structures like backtracking and coroutines.
"""

#
"""
In most implementations of most programming languages, an activation stack is used to implement
procedure calling. At a call, the state of the "caller" (calling procedure) is saved on the stack,
and then control is transferred to the callee.

Because each procedure call requires saving state on the stack, recursion is limited by the stack
depth. In many systems, deep recursions cause stack overflow and program crashes, or use up
unnecessary virtual memory swap space. In most systems, recursion is unnecessarily expensive
in space and/or time. This limits the usefulness of recursion.
"""

#
"""
In Scheme, things are actually simpler. If the last thing a procedure does is to call another
procedure, the caller doesn't save its own state on the stack. When the callee returns,
it will return to its caller's caller directly, rather than to its caller.
After all, there's no reason to return to the caller if all the caller is going
to do is pass the return value along to its caller.

Notice that the relationship between the partial continuations in a full continuation chain
is similar to the relationship between an environment frame and an environment chain.
The former represents control information while the latter represents scope information.
"""

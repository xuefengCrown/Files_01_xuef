
##357
##call graph 289
"""
call-with-current-continuation is a very powerful control construct, which can be used to
create more conventional control constructs, like catch and throw in Lisp (or setjmp and
longjmp in C), or coroutines, and many more. It is extremely powerful because it allows a
program to manipulate its own control "stack" so that procedure calls
and returns needn't follow the normal depth-first textual call ordering.

And since continuations are immutable, they usually form a tree reflecting
the call graph (actually, only the non-tail calls).

If you take a pointer to the current continuation, and put it in a live variable
or data structure, however, then that continuation chain will remain live and not
be garbage collected. That is, you can "capture" the current state of the stack.

If you keep a captured state of the stack around, and later install the pointer to it
in the system's continuation register, then you can return through that continuation chain,
just as though it were a normal continuation. That is, rather than returning to your caller
in the normal way, you can take some old saved continuation and return into that instead!

You might wonder why anybody would want to do such a weird thing to their "stack," but there are
some useful applications. One is coroutines. It is often convenient to structure a computation
as an alternation between two different processes, perhaps one that produces items and another
that consumes them. It may not be convenient to either of those processes into a subroutine
that can be called once to get an item, because each process may have complex state encoded
into its control structure.
"""
##协程提供了什么好处，为什么能提供？

"""
Coroutines allow you to structure cooperating subprograms this way, without making one
subservient to (and callable piecemeal from) another.
"""

##协程实现思路
"""
Coroutines can be implmemented as operations on continuations.
When a coroutine wants to suspend itself and activate another (co-)routine, it simply pushes
a partial continuation to save its state, then captures the value of the continuation register
in some way, so that it can be restored later. To resume a suspended routine,
the continuation chain is restored and the top partial continuation is popped into the
system state registers. Alternation between coroutines is thus accomplished by saving
and restoring the routines' continuations.

"""

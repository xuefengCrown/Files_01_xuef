
##letrec 与 module system
"""
Standard Scheme does not have a module system, but letrec and lambda
are powerful enough to implement modules in portable Scheme.

Suppose we would like to define a module that encapsulates a set of procedures and
variables, but only exports a subset of those procedures.

导出意味着什么？
模块封装了什么？
为什么需要模块？

导入模块，我们导入了什么？
    方法(代码) or 数据
    (没有内部属性的代码作用不大，比如一个计数器就需要维护一个 count-num 属性)
"""

##let*
"""
(define (foo epsilon)
  (let ((a 0)
        (upper (+ a epsilon))
        (lower (- a epsilon)))
...))

这段代码为什么错？

We could fix this by using nested let's, to force evaluation and binding to happen in the
desired order。
"""

##过程调用
"""
In most implementations of most programming languages, an activation stack is used to implement
procedure calling. At a call, the state of the "caller" (calling procedure) is saved on the stack,
and then control is transferred to the callee.

Because each procedure call requires saving state on the stack, recursion is limited
by the stack depth.
"""

##scheme 中的递归
"""
In Scheme, things are somewhat different. As I noted earlier, recursive calls may be
tail recursive, in which case the state of the caller needn't be saved before calling
the callee.
"""

##subproblem
"""
(define (foo)
  (bar) ;;After the call to bar, control must return to foo
  (baz))

(define (baz)
  (bar)
  (foo))
Notice that when foo is called, it does two things: it calls bar and then calls baz.
After the call to bar, control must return to foo, so that it can continue and call baz.
The call to bar is therefore a subproblem--a step in the overall plan of executing foo.
When foo calls baz, however, that's all it needs to do--all of its other work is done.
The result of the call to foo is just the result of foo's call to baz.
"""
##scheme对尾递归的优化
"""
In Scheme, things are actually simpler. If the last thing a procedure does is to call
another procedure, the caller doesn't save its own state on the stack.
When the callee returns, it will return to its caller's caller directly,
rather than to its caller. After all, there's no reason to return to the caller
if all the caller is going to do is pass the return value along to its caller.

Consider both foo and baz above. Neither ever returns--each just calls the other.
In Scheme, these two procedures will repeatedly call each other, without saving their state
on the stack, producing an infinite mutual recursion. Will the stack overflow?
No. Each will save its state before calling bar, but the return from bar will pop
that information off of the stack. The infinite tail-calling between foo and baz will
not increase the stack height at all.
"""

##自由使用递归的好处
"""
Because of this "tail call optimization," you can use recursion very freely in Scheme,
which is a good thing--many problems have a natural recursive structure, and recursion
is the easiest way to solve them.
"""

## implement the tail call optimization yourself.

##区分save caller's state and transferring control to the callee
"""
What's
really going on is that Scheme simply distinguishes between two things that most languages
lump together--saving the caller's state, and actually transferring control to the callee.
Scheme notices that these things are distinct, and doesn't bother to do the former when
only the latter is necessary.

A procedure call is really rather like a (safe) goto that can pass arguments:
control is transferred directly to the callee, and the caller has the option of
saving its state beforehand.

"""

##the continuation chain
"""
In this section, I'll describe a straightforward implementation of Scheme's state-saving
for procedure calling.

In most conventional language implementations, as noted above, calling a procedure allocates an
activation record (or "stack frame") that holds the return address for the call and the variable
bindings for the procedure being called.


Scheme implementations are quite different. As we've explained previously, variable bindings
are not allocated in a stack, but instead in environment frames on the garbage-collected heap.
This is necessary so that closures can have indefinite extent, and can count on the environments
they use living as long as is necessary. The garbage collector will eventually reclaim the space
for variable bindings in frames that aren't captured by closures.

Most Scheme implementations also differ from conventional language implementations in how they
represent the saved state of callers.

(In a conventional language implementation, the callers' state is in two places:
the variable bindings are in the callers' own stack frames,
and the return address is stored in the callee's stack frame.)

In most Scheme implementations, the caller's state is saved in a record on the
garbage-collected heap, called a partial continuation.
It's called a continuation because it says how to resume the caller when we return into it,
how to continue the computation when control returns.

On the other hand, each partial continuation holds a pointer to the partial continuation
for its caller, so a chain of continuations represents how to continue the whole computation:
how to resume the caller, and when it returns, how to resume its caller, and so on until
the computation is complete. This chain is therefore called a full continuation.

(Notice that the relationship between the partial continuations in a full continuation chain
is similar to the relationship between an environment frame and an environment chain.
The former represents control information while the latter represents scope information.)

"""

##cont
"""
the partial continuation that the partial continuation that lets us resume its caller.(继续)

Before we call a procedure, we must save a continuation if we want to resume the current
procedure after the callee returns.

"""


# in java
"""
1) this.x = 3

2) o.x = 3

3) x = 3

前2个是 object mutation. 3)是 variable mutation
"""

#我们使用的语法
"""
box : ('a -> (boxof 'a))
unbox : ((boxof 'a) -> 'a)
set-box! : ((boxof 'a) 'a -> void)
"""
##box takes a value and wraps it in a mutable container.
##unbox extracts the current value inside the container.
##Finally, set-box! changes the value in the container,
##and in a typed language, the new value is expected to
##be type-consistent with what was there before.
##You can thus think of a box as equivalent to a Java container class
##with parameterized type, which has a single member field with a getter and setter:
##box is the constructor, unbox is the getter, and set-box! is the setter.
##(Because there is only one field, its name is irrelevant.)


#引入state和mutation之前，我们求值 plusC时，要先求值它的两个子表达式: l && r
#那时我们不关心 l,r的求值顺序。
#(除非是 dynamic scope模型或者 某个表达式求值会触发错误而中断求值。)
#否则求值 l,不会影响 r的结果。

#现在
"""
当我 (unbox b)时，我不仅要 ask where b is bound,还有看when it is mutated.
状态与时间(time)有关!!!

"""


#关于 env
"""
1. 我们不该copy它，然后传给下个求值过程，这样开销太大
2. 它应该是个stack.(在求值过程中不断 extended && shrink)
"""

## 扩展env
"""
env:   symbol-->location
store: location-->value
"""
#env stays the same, and the store is changing.
##the env says where the box is, and
##the store says what's its value is at the dynamic point of looking it up.


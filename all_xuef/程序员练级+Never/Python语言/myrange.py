# representation
"""
4 是什么?
从物质上来看,它只不过一些散布的像素而已。
从意义上看,它一般表示数量上的四个,这是我们人赋予的。

数字有没有其他表示方式? 我们还可以怎么表示 '四个'?
要知道, 罗马人用 IV 来表示四。
| | | |
(() () () ())
(((())))
f(f(f(f())))
"""

##The Little Schemer和续集The Seasoned Schemer
##The Little Lisper 方法独特以培养读者在 Lisp 中基础的创意的编程技能。
##它循序渐进的包含了学习构造递归和操作递归数据结构所需要的训练和练习。
##程序接受数据和产生数据。设计程序需要对数据有透彻的理解;
##好的程序反映了数据的结构。大多数数据和大多数程序是递归的。
##递归是定义一个对象或者靠自己解决一个问题的行为。
##也许教授递归的最好程序语言就是Scheme

#我们认为写Scheme的递归程序本质上就是简单的模式匹配。
#学习Scheme的关键是“模式匹配”
#The Little Schemer 和 The Seasoned Schemer将不会引导你实际的编程，
#但是掌握书中的这些概念会让你理解计算的本质。

# What does (* n m) do? It builds up a number by adding n up m times.

# 计算的本质
""" 最基本的操作: +1, -1

    加法(n+m)是什么: 不断的 +1
    乘法(n*m)是什么: 不断的 +n
    指数(n**m)是什么: 不断的 *n
"""
# 我们可以基于 +1, -1 操作来定义加法、乘法和指数运算;
# 如下: (n,m >= 0)
def add(n,m):
    return m if n==0 else add((n-1), (m+1))

def mul(n,m):
    return 0 if m==0 else add(n, mul(n,(m-1)))

def power(n,m):
    return 1 if m==0 else mul(n, mul(n, (m-1)))

# 进一步的, 我们可以定义 >, <
def gt(n,m): # >
    if n==0: return False
    if m==0: return True
    return gt((n-1), (m-1))

def lt(n,m): # <
    if m==0: return False
    if n==0: return True
    return lt((n-1), (m-1))

print(mul(3,0))
print(power(3,0))
print(gt(2,1))
print(lt(1,2))
def my_sum(iterable):
    if not iterable:
        return 0
    else:
        return add(iterable[0], my_sum(iterable[1:]))
    
# 如果不想用内置range,可以自定义一个
def my_range(start, stop, step):
    if start >= stop:
        return []
    else:
        return [start] + my_range(add(start,step), stop, step)

print(my_sum(my_range(1,101,1)))
#print(my_range(1, 101, 2))

"""
(* 12 3)
=  12 + (* 12 2)
=  12 + 12 + (* 12 1)
=  12 + 12 + 12 + (* 12 0)
=  12 + 12 + 12 + 0
"""

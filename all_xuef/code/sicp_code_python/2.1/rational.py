"""
有理数系统
"""
# 抽象屏障的思想使程序很容易维护和修改
# 数据抽象方法使我们能推迟决策的时间，而又不会阻碍系统其它部分的工作进展

# 数据意味着什么?
"""
一般而言，我们总可以将数据定义为一组适当的选择函数和构造函数，以及
为使这些过程成为一套合法表示，它们就必须满足的一组特定条件。

在这里(有理数)，我们要保证，如果从一对整数n和d构造出一个有理数x，
那么，抽取出x的numer和denom并将它们相除，得到的结果应该等于n除以d。
换句话说，make_rat, numer和denom必须满足：
对任意整数n和任意非零整数d，如果x是make_rat(n, d)，那么：
(numer x)/(denom x) = n/d
"""

def gcd(m, n):
    "m, n最大公约数"
    if m%n == 0: return n
    return gcd(n, m%n)
def make_rat(n, d):
    # TODO
    # 规范化; 能够处理正数和负数
    if d < 0: n = -n
    return (n, d)
def numer(r):
    return r[0]
def denom(r):
    return r[1]
def opp_rat(x):
    return make_rat(-numer(x), denom(x))
def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    n, d = nx*dy + ny*dx, dx*dy
    g = gcd(n, d)
    return make_rat(n//g, d//g)
def sub_rat(x, y):
    return add_rat(x, opp_rat(y))

def display(rat):
    print(numer(rat), "/", denom(rat))

one_half = make_rat(1, 2)
one_third = make_rat(1, 3)

display(add_rat(one_half, one_third))
display(add_rat(one_third, one_third))
display(opp_rat(one_half))
display(sub_rat(one_half, one_third))


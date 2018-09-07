
"""
序对是什么？
cons, car, cdr

如果用cons将两个对象粘结在一起，那么就可以借助于car和cdr提取这两个对象;
任何能满足上述条件的三个过程都可以成为实现序对的基础。
"""
# 下面的事实说明：我们完全可以不用任何数据结构，只使用过程就可以实现序对;

"""
这些东西看起来好像只是很好玩，但实际上，数据的过程性表示将在
我们的程序设计宝库中扮演一种核心的角色。
有关的程序设计风格通常称作消息传递。
"""
# 消息传递

def cons(x, y):
    def dispatch(m): # m is message's m
        if m == 0: return x
        if m == 1: return y
        else: return None
    # 返回一个过程 
    return dispatch
def car(pair):
    return pair(0)
def cdr(pair):
    return pair(1)

pair = cons(1,2)
print(car(pair))
print(cdr(pair))



from ucb import trace, main, interact
from operator import add, sub, mul, truediv
from scheme_reader import Pair, nil, scheme_read, buffer_input

# (+ 1 (* 2.3 45))
tokens = ['(', '+', 1, '(', '*', 2.3, 45, ')', ')']

"""
基于以上tokens构建AST
1. 使用栈
2. 互相调用的递归
scheme_read
read_tail

以上针对的是前缀表达式(scheme)

对于中缀表达式, 可以使用基于BNF范式构建的递归下降分析器来构建AST
"""

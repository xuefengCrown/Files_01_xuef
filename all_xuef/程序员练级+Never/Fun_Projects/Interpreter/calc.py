#计算器 (* (+ 2 2) (+ 3 4))
def tokenize(code_s):   #词法分析:-->tokens
    return code_s.replace('(', ' ( ').replace(')', ' ) ').split()

def analyze(toks):      #语法分析:-->表达式树
    def analyze_tok(tok):
        """Return the value of token if it can be analyzed as a number, or token."""
        try:
            return int(tok)
        except (TypeError, ValueError):
            return tok
    def get_operands(toks): # 2 2)-->[2 2]
        operands,tok = [],toks[0]
        while tok != ')':
            operands.append(analyze(toks))
            tok = toks[0]
        toks.pop(0) # pop ')'
        return operands
    tok = analyze_tok(toks.pop(0))
    #表达式树是一种结构化数据，为了简洁我这里使用嵌套list
    return tok if type(tok) in (int,) else [toks.pop(0), get_operands(toks)]
            
from operator import mul,truediv,sub; from functools import reduce
cxt = {'+': sum, '-': sub, '*': (lambda args:reduce(mul,args)), '/': truediv}

def calc_eval(expr_tree): #求值
    if not isinstance(expr_tree, list): return expr_tree
    opt = expr_tree[0]
    if opt in ('+','*'): return cxt[opt]([calc_eval(exp) for exp in expr_tree[1]])
    return cxt[opt](*[calc_eval(exp) for exp in expr_tree[1]])
    
c = "(* (+ 2 2) (+ 3 4))"
res = calc_eval(analyze(tokenize(c))) # ['*', [['+', [2, 2]], ['+', [3, 4]]]]
print(res)

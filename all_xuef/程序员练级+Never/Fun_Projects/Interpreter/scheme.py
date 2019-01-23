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
    if type(tok) in (int,) or tok not in ('(',')'):
        return tok
    elif toks[0] == '(':
        return get_operands(toks)
    else:
        res = [toks.pop(0)]
        res.extend(get_operands(toks))
        return res

#############################
#对环境(environment)的基本操作
#############################
env0 = [] # empty env
def extend_env(var,val, env):
    env_copy = env[:]
    env_copy.insert(0, (var,val))
    return env_copy
def lookup(env, var):
    if not env:
        raise Exception("Unbind Variable:{v}".format(v=var))
    return env[0][1] if env[0][0] == var else lookup(env[1:], var) # 向外层env寻找

from operator import mul,truediv,sub; from functools import reduce
context = {'+': sum, '-': sub, '*': (lambda args:reduce(mul,args)), '/': truediv}

# 求值
is_number = lambda exp: type(exp) in (int,float)
is_symbol = lambda exp: not any([is_number(exp), isinstance(exp, list)])
SUPPORT_BASE_OPS = context.keys() # 支持的基本算术操作

class Closure: # 表示一个函数定义
    def __init__(self, var, body, env):
        self.var = var
        self.body = body
        self.env = env


def scheme_eval(exp_tree, env=env0):
    if is_number(exp_tree):                         # 数字
        return exp_tree
    elif is_symbol(exp_tree):                       # symbol(变量或者代表函数的符号)
        if exp_tree == 'globals':
            return env0
        return lookup(env, exp_tree)
    elif exp_tree[0] == 'lambda':                   # 函数定义
        var = exp_tree[1][0]
        body = exp_tree[2]
        #print("create a closure: var:{v}, body:{b}, env:{e}".format(v=var,b=body,e=env))
        return Closure(var, body, env)
    elif exp_tree[0] == 'let':                      # 绑定
        bindings = exp_tree[1]
        new_env = env[:]
        for bind in bindings:
            new_env = extend_env(bind[0], scheme_eval(bind[1], env), new_env)
        e = exp_tree[2]
        return scheme_eval(e, new_env)
    elif exp_tree[0] == 'define':
        _,var,exp = exp_tree
        val = scheme_eval(exp, env)
        env.insert(0, (var,val))
        return val
    elif not(type(exp_tree[0]) == list) and exp_tree[0] in SUPPORT_BASE_OPS: # 算术表达式
        if exp_tree[0] in ('+','*'):
            return context[exp_tree[0]]([scheme_eval(e, env) for e in exp_tree[1:]])
        else: return context[exp_tree[0]](*[scheme_eval(e, env) for e in exp_tree[1:]])
    else:                                           # Procedure Call
        proc = scheme_eval(exp_tree[0], env)
        param = scheme_eval(exp_tree[1], env)
        return scheme_eval(proc.body, extend_env(proc.var, param, proc.env))
    raise Exception("Not Support OP!")

def r2(code):
    return scheme_eval(analyze(tokenize(code)),
                       env0)

# repl
def repl(prompt='> '):
    while True:
        val = r2(input(prompt))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "将一个Python对象转换回可以被Scheme读取的字符串。"
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    
if __name__ == '__main__':
    #repl()
    print(analyze(tokenize("'(1 (+ 2 3) 8)")))


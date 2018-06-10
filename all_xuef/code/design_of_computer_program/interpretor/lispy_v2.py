#coding:utf-8


"""
(version 2 -- a full lispy)an interpreter of scheme in python(3.6)
"""

"""
what a language interpreter does?
    program --> |parse| --> abstract-syntax-tree --> |eval| --> result
"""

# type definitions
Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List

Env    = dict             # A Scheme environment (defined below) 
                          # is a mapping of {variable: value}


# parse
def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def parse(program: str) -> Exp:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

"""
本来觉得read_from_tokens有点麻烦，就想用map写个简单版本read_from_tokens_sim;
发现，python没有能处理嵌套列表的map, 于是还得写个map_rec;
最后发现不光麻烦，而且与read_from_tokens相比，速度有点慢。
所以，这里还是使用了read_from_tokens。
"""
def read_from_tokens_sim(tokens: list) -> Exp:
    return list(map_rec(atom, tokens))

## 这个递归函数写的我有点糊涂，有空改写
def map_rec(fn, lst_rec: list):
    "将函数 fn 作用于 lst_rec(层级结构) 的所有元素上"
    if len(lst_rec) == 0: return []
    
    first_ele = lst_rec[0]
        
    if type(first_ele) is list:
        return [map_rec(fn, first_ele)] + list(map_rec(fn, lst_rec[1:]))
    elif type(first_ele) in (str, int, float):#Atom:
        if map_rec(fn, lst_rec[1:]) == []:
            return [fn(first_ele)]
        else:
            return [fn(first_ele)] + list(map_rec(fn, lst_rec[1:]))
    
def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    # xuef一点思考：
    # 异常也能够起到条件语句的功能
    # 其实考察if的本质，就是根据条件的不同进行值或动作的转发。
    # 因为在python中函数可以作为字典的值，所以dict也能实现if的动作转发功能。
    # 而在java中，函数不能作为孤立的值，它需要作为对象的方法来保存。
    # 你想实现动作转发，需要转发到相应的对象，于是有了设计模式之策略模式。
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


# Environments
import math
import operator as op

def standard_env() -> Env:
    "An environment with some Scheme standard procedures."
    # 因为python简直可以看做lisp的一个方言，所以这里的env可以很简洁的表达出来。
    # 可以去看一下Peter Norvig的一篇比较python与lisp的文章。
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),  
	'print':   print,
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env

########################## version2 add ################################
class Env(dict):
    "An environment: a dict of {'var': val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

class Procedure(object):
    "A user-defined Scheme procedure."
    # env 为此过程当前所在环境
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        # Env生成一个当前环境的子环境
        return eval(self.body, Env(self.parms, args, self.env)) 
########################## version2 add ################################

global_env = standard_env()


# Evaluation
"""
注意表达式是递归结构的 ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
"""
def eval2(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):    # variable reference
        return env.find(x)[x]
    elif isinstance(x, Number):  # constant 
        return x   
    op, *args = x    # args是个tuple，收集余下所有参数
    # (quote (+ 1 2)) --> (+ 1 2)
    if op == 'quote':            # quotation
        return args[0]
    ## 很漂亮的代码，值得学习：包括解包和条件表达式的运用。
    elif op == 'if':             # conditional
        (test, conseq, alt) = args
        exp = (conseq if eval2(test, env) else alt)
        return eval2(exp, env)
    # (define var exp)所做的，是向全局环境注入变量var->exp的映射
    # 理解一门语言的语法的最佳办法是，写一个该语言的解释器(或编译器)
    elif op == 'define':         # definition
        (symbol, exp) = args
        # define 时，要对exp求值的
        env[symbol] = eval2(exp, env)
    elif op == 'set!':           # assignment
        (symbol, exp) = args
        env.find(symbol)[symbol] = eval2(exp, env)
    # (define circle-area (lambda (r) (* pi (* r r)))
    # 注意，lambda时没有继续向内求值
    elif op == 'lambda':         # procedure
        (parms, body) = args
        return Procedure(parms, body, env)
    else:                        # procedure call
        # begin 也会到这里，计算其每个表达式的值，收集进列表vals，然后执行begin(*vals)。
        # begin所做的是，返回最后一个值。
        # 这正是lisp中progn的逻辑---依次执行表达式，返回最后一个表达式的值。

        # 注意，op 只是函数的名字(symbol)而已，真正的函数对象(实体)存储在global_env中，
        # 所以需要对该函数符号进行求值(eval)
        proc = eval2(op, env)
        # 告诉了我们，函数调用时都做了些什么。
        # 先要对该函数的每个参数(可能是表达式)进行求值，然后将值收集起来传递给函数调用。
        vals = [eval2(arg, env) for arg in args]
        return proc(*vals) # args是个列表(list)，所以要先解包
    

# Interaction: A REPL
def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        exp = input(prompt)
        if(exp == "quit" or exp == "exit"): break
        val = eval2(parse(exp))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        # 注意schemestr是递归的
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    

def test():
    # 这里，* 只支持两个参数。(* 3.14 x x)会出错。
##    program = "(begin (define r 10) (* pi (* r r)))"
##
##    parse_result = parse(program)
##
##    print(parse_result)
##    print(eval(parse_result))
##    res = map_rec(math.sqrt, [4,[9], 16, [25, 36]])
##    print(res)
    repl()
if __name__ == '__main__':
    test()

















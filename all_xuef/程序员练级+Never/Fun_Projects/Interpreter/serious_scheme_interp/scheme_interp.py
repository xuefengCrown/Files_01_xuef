#############################
#Scheme-->Python 类型映射
#方便以后扩展或修改
#?如何区分 string和Symbol?
#############################
Symbol = str            # Scheme符号由 Python str表示
List   = list           # Scheme列表由 Python list表示
Number = (int, float)   # Scheme数字由 Python的整数或浮点数表示
BoolV = (True, False)

#############################
#对环境(environment)的基本操作
#############################
class Env():
    def __init__(self, bindings, parent_env=None):
        self.bindings = bindings
        self.parent_env = parent_env
    def extend(self, var, val):
        self.bindings[var] = val
        
    def lookup(self, var):
        if var in self.bindings:
            return self.bindings[var]
        elif self.parent_env is not None:
            return self.parent_env.lookup(var)
        else:
            raise("unbind variable: {var}!".format(var=var))
    def __str__(self):
        if self.bindings is None:
            return "{}"
        else:
            return '{' +str(self.bindings) + ', penv: ' + str(self.parent_env) + '}' 
#############################
#初始化全局环境
#############################
from operator import add,mul,truediv,sub
from functools import reduce
from scheme_builtins import BUILTINS # scheme builtin-proc package

top_level_binds = {'+': (lambda *args:reduce(add,args)), '-': sub,
                   '*': (lambda *args:reduce(mul,args)), '/': truediv}
top_level_binds.update(BUILTINS)        # 将内置函数包加入到全局环境
top_level_env = Env(top_level_binds)    # 初始化全局环境
## 支持的基本算术操作
PRIMITIVES = top_level_binds.keys() 

#############################
#为函数定义和调用提供支持
#############################
class Closure: # 函数作为闭包
    def __init__(self, args, body, cenv):
        self.args = args
        self.body = body
        self.cenv = cenv
    def __call__(self, *args):
        return interp(self.body,
                      Env(dict(zip(self.args, args)),
                          self.cenv))#注意这里扩展的是cenv
    def __str__(self):
        return "a closure:\n args:{v},\n body:{b},\n env:{e}".format(v=self.args,
                                                               b=self.body,
                                                               e=self.cenv)
        
########################
#exp类型判断
########################
def self_evaluating(e): 
    if type(e) != List:
        return type(e) in Number or e in BoolV
    return False
         
def is_symbol(e):
    return type(e) == Symbol
    
## combination OR special form (any parenthesized expr)
def is_pair(e):
    return type(e) == List


########################
#do special form
########################
SPECIAL_FORM = ['if','lambda', 'let', 'define', 'quote', 'quasiquote']
def is_special_form(e):
    return e[0] in SPECIAL_FORM

def do_if(e, env):
    test = interp(e[1], env)
    # 这里假设 if 表达式有三个分支
    if test is True:
        # 注意，这里一定不能先对分支求值
        # 否则 (if #f (/ 1 0) 0)会raise error
        return interp(e[2], env)
    else:
        return interp(e[3], env)
    
# 处理函数定义
def do_lambda(e, env):
    return Closure(e[1], e[2], env)

# 处理绑定(let是语法糖，其实可规约到lambda调用)
## (let ((x 1) (y 2)) (+ x y)) === ((lambda (x y) (+ x y)) 1 2)
def do_let(e, env):
    new_env = Env({let[0]:interp(let[1],env) for let in e[1]}, env)
    return interp(e[2], new_env)

def do_define(e, env):
    env.extend(e[1], interp(e[2], env))
    return e[1]
def do_quote(e, env):
    pass
def do_quasiquote(e, env):
    pass

SPECIAL_FORM_FUNC = [do_if, do_lambda, do_let, do_define, do_quote, do_quasiquote]
SPECIAL_FORM_DICT = dict(zip(SPECIAL_FORM, SPECIAL_FORM_FUNC))
def eval_special_form(e, env):
    return SPECIAL_FORM_DICT[e[0]](e, env)

def eval_compound(e, env):
    "求值复合表达式"
    if is_special_form(e):
        return eval_special_form(e, env)
    else: # 函数调用
        #pdb.set_trace()
        proc = interp(e[0], env)
        params = [interp(sube, env) for sube in e[1:]]
        # TODO: 参数是否匹配
        return proc(*params)
    
## 解释器主函数    
def interp(exp_tree, env=top_level_env):
    if self_evaluating(exp_tree):   # Number OR Bool
        return exp_tree
    elif is_symbol(exp_tree):       # symbol(变量或者代表函数的符号)
        if exp_tree == 'globals':
            return top_level_env
        if exp_tree == 'builtins':
            return PRIMITIVES
        return env.lookup(exp_tree)
    elif is_pair(exp_tree):         # 复合表达式(combination OR special form)
        return eval_compound(exp_tree, env)
    else:
        raise Exception("Illegal Expression!", exp_tree)
    

from recursive_descent_parse import SexpParser
##解释器的"用户界面"
def pscm(code):
    return interp(SexpParser().parse(code),
                       top_level_env)

## repl
def repl(prompt='> '):
    while True:
        code = input(prompt)
        val = pscm(code)
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "将一个Python对象转换回可以被Scheme读取的字符串。"
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    
if __name__ == '__main__':
    repl()

    
"""
(define fib (lambda (n) (if (< n 3) 1 (+ (fib (- n 2)) (fib (- n 1))))))

(let ((x 2))
  (let ((f (lambda (y) (* x y))))
    (let ((x 4))
      (f 3))))

(let ((x 2)) (let ((f (lambda (y) (* x y)))) (let ((x 4)) (f 3))))
--> 6
"""

#TODO (can easily be extended)
"""
self-evaluating?
symbol?
combination OR special form

我们现在使用 list来表示 AST，我们需要提供一套选择函数和谓词检测，以方便以后
的扩展或修改。(比如使用 Pair来表示抽象语法树)

;; 下面的代码就易于扩展?!
(define (special-form-name? expr)
    (member '(if define set!)))

eval-special-form just dispatches again, calling a routine that handles whatever kind
of special form it's faced with.
(Later, we'll see prettier ways of doing this kind of dispatching, using first-class procedures.)

如何处理 #f,#t?是否使用python内置类型来表示它?

Implementing top-level variable bindings
1. 如何表示
2. 每次扩展时是否创建新环境？还是就地修改(类似一个 stack)？
3. 顶层环境中应该设置哪些东西？
The interpreter maintains a pointer to the "current environment" when evaluating an expression. This
pointer always points to the environment the currently-executing code must execute in, i.e., the variable
bindings it must see for the variables it uses. When we evaluate a variable, we look for a binding of its
name in the current environment, by searching up the environment chain starting from the "current
environment" pointer.

After entering the let and creating the bindings for x and y, the interpreter changes the environment
pointer to point to the resulting new environment. This is typically implemented by representing the
environment as a chain of tables called frames, rather than a simple flat table.

This environment chain is used as a pointer-linked stack, for the most part,
with new frames being pushed onto the stack when a let is entered, and popped off
the stack when a let is exited.



error checking

"""

# frame
"""
    bindings
    parent_env
Each frame holds bindings created by a particular binding construct in the program, e.g., on
entering a let. A whole environment is not represented by just one frame, but by the chain of
frames starting at a particular frame.
The environment inherits bindings from the environment it's scoped inside.

(let ([x 1] [y 2])
    (+ x y))
处于顶层环境中，它会基于顶层环境来创建一个新环境。
"""

# eval
##we're executing an expression in an environment.这是完整的表述

#???
##When we exit the let, the current environment pointer is set back to point to
##the same environment frame as before entering the let.

##Keep in mind that an environment is a language-level entity, and just consists of
##a set of bindings; it is just a mapping from names to storage that can hold values. 

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
实现可以计算像 7 + 3 * (10 / (12 /(3 + 1)- 1))
这样任意深度嵌套的括号表达式的解释器。
为表达式构建抽象语法树(AST)。
"""
import re
import collections
###############################################################################
#                                                                             #
#  LEXER                                                                     #
#                                                                             #
###############################################################################
# Token specification
## ?P<TOKENNAME> 用于给一个模式命名，供后面使用。
NUM = r'(?P<NUM>\d+)' 
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIV = r'(?P<DIV>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIV, LPAREN, RPAREN, WS]))
# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    """生成令牌流"""
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################   
import operator as op
op_tab = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

"""
    >>> mul_token = Token(MUL, '*')
    >>> plus_token = Token(PLUS, '+')
    >>> mul_node = BinOp(
    ...     left=Num(Token(NUM, 2)),
    ...     op=mul_token,
    ...     right=Num(Token(NUM, 7))
    ... )
    >>> add_node = BinOp(
    ...     left=mul_node,
    ...     op=plus_token,
    ...     right=Num(Token(NUM, 3))
    ... )
"""
class AST(object):
    pass
class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
"""
文法
expr: term((PLUS|MINUS)term)*
term: factor((MUL|DIV)factor)*
factor: NUM |(expr)
"""
class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.cur_tok = next(self.tokens, None)
        
    def err(self):
        raise Exception('Invalid syntax')
    def nxt_tok(self):
        #print(self.cur_tok)
        self.cur_tok = next(self.tokens, None)
        
    def eat(self, tok_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.cur_tok.type == tok_type:
            self.nxt_tok()
        else: self.err()
        
    def term(self):
        """ term: factor((MUL|DIV)factor)* """
        node = self.factor()
        while self.cur_tok and self.cur_tok.type in ['TIMES','DIV']:
            tok = self.cur_tok
            if tok.type == 'TIMES':
                self.eat('TIMES')
            elif tok.type == 'DIV':
                self.eat('DIV')
            node = BinOp(left=node, op=tok, right=self.factor())
        return node
    
    def factor(self):
        """factor : NUM | LPAREN expr RPAREN"""
        tok = self.cur_tok
        if tok.type == 'NUM':
            self.eat('NUM')
            return Num(Token(tok.type, int(tok.value)))
        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
    
    def expr(self):
        """ expr: term((PLUS|MINUS)term)* """
        node = self.term()
        while self.cur_tok and self.cur_tok.type in ['PLUS','MINUS']:
            tok = self.cur_tok
            if tok.type == 'PLUS':
                self.eat('PLUS')
            elif tok.type == 'MINUS':
                self.eat('MINUS')
            node = BinOp(left=node, op=tok, right=self.term())
        return node
    def parse(self):
        """ return a AST represents given expression """
        return self.expr()
class Interpreter():
    def __init__(self, parser):
        self.parser = parser
    def eval_ast(self, node):
        if node.token.type == 'NUM':
            return node.value
        return op_tab[node.op.value](self.eval_ast(node.left), self.eval_ast(node.right))
##        if node.op.type == 'PLUS':
##            return self.eval_ast(node.left) + self.eval_ast(node.right)
##        elif node.op.type == 'MINUS':
##            return self.eval_ast(node.left) - self.eval_ast(node.right)
##        elif node.op.type == 'TIMES':
##            return self.eval_ast(node.left) * self.eval_ast(node.right)
##        elif node.op.type == 'DIV':
##            return self.eval_ast(node.left) / self.eval_ast(node.right)
    def interpret(self):
        tree = self.parser.parse()
        return self.eval_ast(tree)
    def rpn(self):
        """输入一个数学表达式，并以后缀表达式（也就是逆波兰表达式，RPN）的形式输出它"""
        # 左-->右-->根 (后序遍历)
        def postorder(node):
            # 叶子节点
            if node.token.type == 'NUM':
                print(node.value, end=' ')
                return
            postorder(node.left)
            postorder(node.right)
            print(node.op.value, end=' ')
        postorder(self.parser.parse())
        print()
    def lsp(self):
        """输入一个数学表达式，并以LISP风格输出它"""
        # 根-->左-->右 (先序遍历)
        def preorder(node):
            # 叶子节点
            if node.token.type == 'NUM':
                print(' ', end='')
                print(node.value, end='')
                return
            print(' (', end='')
            print(node.op.value, end='')
            preorder(node.left)
            preorder(node.right)
            print(')', end='')
            
        preorder(self.parser.parse())
        print()
def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('spi> ')
            if text in ['q','quit','exit']: break
        except EOFError:
            break
        if not text:
            continue
##        tokens = generate_tokens(text)
##        parser = Parser(tokens)
##        interpreter = Interpreter(parser)
##        print('postfix expr: ', end='')
##        interpreter.rpn()

##        tokens = generate_tokens(text)
##        parser = Parser(tokens)
##        rs = interpreter.interpret()
##        print(text, ' = ', rs)
        tokens = generate_tokens(text)
        parser = Parser(tokens)
        interpreter = Interpreter(parser)
        print('lsp expr: ', end='')
        interpreter.lsp()

if __name__ == '__main__':
    main()



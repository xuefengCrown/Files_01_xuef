#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
一个 interpreter 来处理像“7 + 5 * 2”这样的算术表达式
"""
import re
import collections

# Token specification
## ?P<TOKENNAME> 用于给一个模式命名，供后面使用。
NUM = r'(?P<NUM>\d+)' 
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIV = r'(?P<DIV>/)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIV, WS]))
# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    """生成令牌流"""
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok
    
import operator as op
op_tab = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}


"""
文法
expr: term((PLUS|MINUS)term)*
term: factor((MUL|DIV)factor)*
factor: NUM
"""
class Calc(object):
    def __init__(self, tokens):
        self.cur_tok = None
        self.tokens = tokens
    def err(self):
        raise Exception('Invalid syntax')
    def nxt_tok(self):
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
        res = self.factor()
        while self.cur_tok and self.cur_tok.type in ['TIMES','DIV']:
            tok = self.cur_tok
            if tok.type == 'TIMES':
                self.eat('TIMES')
                res = res * self.factor()
            elif tok.type == 'DIV':
                self.eat('DIV')
                res = res / self.factor()
        return res
    
    def factor(self):
        """ factor: NUM """
        tok = self.cur_tok
        self.eat('NUM')
        return int(tok.value)
    
    def expr(self):
        """ expr: term((PLUS|MINUS)term)* """
        self.nxt_tok()
        res = self.term()
        while self.cur_tok and self.cur_tok.type in ['PLUS','MINUS']:
            tok = self.cur_tok
            if tok.type == 'PLUS':
                self.eat('PLUS')
                res = res + self.term()
            elif tok.type == 'MINUS':
                self.eat('MINUS')
                res = res - self.term()
        return res

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
            if text in ['q','quit','exit']: break
        except EOFError:
            break
        if not text:
            continue
        tokens = generate_tokens(text)
        calc = Calc(tokens)
        rs = calc.expr()
        print(text, ' = ', rs)

if __name__ == '__main__':
    main()



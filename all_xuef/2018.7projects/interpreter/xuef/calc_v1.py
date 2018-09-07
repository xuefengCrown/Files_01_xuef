#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
一个 interpreter 来处理像“7 – 3 + 2 – 1”这样的算术表达式
"""
import re
import collections

# Token specification
## ?P<TOKENNAME> 用于给一个模式命名，供后面使用。
NUM = r'(?P<NUM>\d+)' 
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, WS]))
# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    "生成令牌流"
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok
    
import operator as op
op_tab = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

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
        tok = self.cur_tok
        self.eat('NUM')
        return int(tok.value)
    def expr(self):
        self.nxt_tok()
        res = self.term()
        while self.cur_tok and self.cur_tok.type in ['PLUS','MINUS','TIMES','DIVIDE']:
            tok = self.cur_tok
            operator = op_tab[self.cur_tok.value]
            self.eat(self.cur_tok.type)
            res = operator(res, self.term())
        return res

##    head, *tail = tokens
##    if not tail: return int(head.value)
##    return op_tab[tail[0].value](int(head.value), expr(tail[1:]))
   
def main():
    #text = "7 - 3 +  2 -1"
    #text = "3 - 4 + 5 -1"
    #text = "10 + 1 + 2 - 3 + 4 + 6 - 15"
    # 在普通的算术运算和大部分编程语言中，加法、减法、乘法和除法都是左结合的
    """
    7 + 3 + 1 is equivalent to (7 + 3) + 1
    7 - 3 - 1 is equivalent to (7 - 3) - 1
    8 * 4 * 2 is equivalent to (8 * 4) * 2
    8 / 4 / 2 is equivalent to (8 / 4) / 2
    """
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



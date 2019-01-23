
"""
The reader is a simple kind of recursive descent parser for normal Scheme data structures.
(A parser converts a sequence of tokens into a syntax tree that
describes the nesting of expressions or statements.)

It is a "top-down" parser, because it recognizes high-level structures before
lower-level ones--e.g., it recognizes the beginning of a list before reading
and recognizing the items in the list.
(That is, on seeing a left parenthesis, it "predicts" that it will see sequence
of list elements followed by a matching right parenthesis.)
"""
##The reader converts a linear sequence of characters into a simple parse tree.
##A parse tree represents the syntactic structure (phrase groupings) of a sequence of characters.

#S-exp EBNF
"""
S-list ::= ({ S-exp }∗)
S-exp ::= Symbol | S-list
"""
from tokenize_scheme import generate_tokens

class SexpParser():
    '''
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the ._expect()
    method to exactly match and discard the next token on the input
    (or raise a SyntaxError if it doesn't match).
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenized
        self._advance()  # Load first lookahead token
        
        return self.sexp()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammar rules follow
    def sexp(self):
        "S-exp ::= Symbol | S-list"
        if self._accept('INTEGER'):
            return int(self.tok.value)
        elif self._accept('FLOAT'):
            return float(self.tok.value)
        elif self._accept('BOOLEAN'):# TODO
            return {'#t': True, '#f': False}[self.tok.value]
        elif self._accept('SYMBOL') or self._accept('STRING') or \
             self._accept('CHARACTER'):
            return self.tok.value
        else:
            return self.slist()
            
    def slist(self):
        "S-list ::= ({ S-exp }∗)"
        s = []
        self._accept('LPAREN')
        while not self._accept('RPAREN'):
            sube = self.sexp()
            s.append(sube)
        return s[:]
def descent_parser():
    parser = SexpParser()
    print(parser.parse('2'))
    print(parser.parse('(+ 1 2 3)'))
    print(parser.parse('(lambda (x) (* x (+ x 1)))'))
    print(parser.parse('(let ((x 1) (y 2)) (+ x y))'))
    print(parser.parse('(if (> x 3) 1 0)'))
    print(parser.parse('(define area (* a a))'))
    print(parser.parse('(proc (* y y) (* x x))'))
if __name__ == '__main__':
    descent_parser()

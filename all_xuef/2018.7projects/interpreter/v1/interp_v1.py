# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
import operator as op
INTEGER, PLUSSUB, EOF = 'INTEGER', 'PLUSSUB', 'EOF'
ope_tab = {'+': op.add, '-': op.sub}
"""
一个记号（token)是一对类型·值

将输入的字符串切分成记号的过程被称作词法分析。
所以，第一步解释器需要读取输入并把它转换成一系列的记号。
解释器做这部分工作的组件被称作词法分析器（lexical ananlyzer，简称lexer）。
你也许碰到过其它的叫法，像扫描程序（scanner)，分词器（tokenizer)。
它们意思都相同：解释器或者编译器中把输入字符串转换成一串记号的组件。
"""
class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char in ['+','-']:
            token = Token(PLUSSUB, current_char)
            self.pos += 1
            return token
        
        # 1. 处理输入字符串中的空白字符
        if current_char == ' ' or current_char == '': 
            self.pos += 1
            return self.get_next_token()

        self.error() # 解析失败

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """ expr -> INTEGER PLUS INTEGER
            expr 方法首先试图识别（parsing）token 流中的 INTEGER -> PLUS -> INTEGER
            或 INTEGER -> MINUS -> INTEGER 短语，成功完成识别（parsed）其中一种短语后，
            该方法解释它，并将两整数相加或相减的结果返回给调用者。
        """
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(PLUSSUB)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = ope_tab[op.value](left.value , right.value)
        return result

"""
为了让计算器工作正常，不抛出异常，输入应该遵循几条规则：
1. 输入只能是个位数的整数
2. 当前支持的算术运算只有加法
3. 在输入中不允许出现空格
"""
import re
def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
            if text in ['quit','q','exit']: break
            text = re.split(r'([\+\-\s])',text)
            print(text)
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()

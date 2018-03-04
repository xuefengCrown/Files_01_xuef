"""
a = LeafNode(4)
b = InteriorNode(’+’, LeafNode(2), LeafNode(3))
"""

class LeafNode(object):
    """Represents an integer."""
    def __init__(self, data):
        self. data = data
    def postfix(self):
        return str(self)
    def __str__ (self):
        return str(self. data)

class InteriorNode(object):
    """Represents an operator and its two operands."""
    def __init__(self, op, leftOper, rightOper):
        self.operator = op
        self.leftOperand = leftOper
        self.rightOperand = rightOper
    def postfix(self):
        return self.leftOperand.postfix() + " " + \
                self.rightOperand.postfix() + " " + \
                self.operator

class ExpressionTree():
    def __init__(self):
        pass
    # Syntax rule:
    # factor = number | "(" expression ")"
    def factor(self):
        token = self.scanner.get()
        if token.getType() == Token.INT:
            tree = LeafNode(token.getValue())
            self.scanner.next()
        elif token.getType() == Token.L_PAR:
            self.scanner.next()
            tree = self.expression()
            self.accept(self.scanner.get(), Token.R_PAR, "')'expected")
            self.scanner.next()
        else:
            tree = None
            self.fatalError(token, "bad factor")
        return tree

a = LeafNode(4)
b = InteriorNode('+', LeafNode(2), LeafNode(3))
c = InteriorNode('*', a, b)
c = InteriorNode('-', c, b)
#print("Expect ((4 * (2 + 3)) - (2 + 3)) :", c.infix())
#print("Expect - * 4 + 2 3 + 2 3 :", c.prefix())
print("Expect 4 2 3 + * 2 3 + - :", c.postfix())
#print("Expect 15 :", c.value())
























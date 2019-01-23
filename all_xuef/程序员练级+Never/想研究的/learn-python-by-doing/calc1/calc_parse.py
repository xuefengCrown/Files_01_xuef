
import ast
class MyVisitorException(Exception):
  pass


class Walker(ast.NodeVisitor):
    op_mapping = {'Add':'+', 'Sub':'-', 'Mult':'*',
                  'Div':'/', 'FloorDiv':'//', 'USub':'--'}
    def generic_visit(self, n):
        node_name = n.__class__.__name__
        if node_name == 'Module':
            return self.visit(n.body[0])
        elif node_name == 'Expr':
            return self.visit(n.value)
        elif node_name == 'BinOp':
            opn = Walker.op_mapping[n.op.__class__.__name__]
            return [opn, self.visit(n.left), self.visit(n.right)]
        elif node_name == 'UnaryOp':
            opn = Walker.op_mapping[n.op.__class__.__name__]
            return [opn, self.visit(n.operand)]
        else:
            return n.n

def exp2ast(exp: str)->list:
    """
    exp2ast(exp: str)->list
      consume a arithmetic expression, it will produce a nested list
      that represents the abstract syntax tree of the arith exp.
    """
    return Walker().visit(ast.parse(exp))
    
if __name__ == '__main__':
  from pprint import pprint
  import sys
  print(exp2ast.__doc__)
  pprint(exp2ast(sys.stdin.read()))


import operator as op

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    def div(b,a): # 除法趋零取整
        if a*b < 0: return -(-b//a)
        return b//a
    #s, tb = [], {'+':op.add, '-':op.sub, '*':op.mul, '/':div}
    s, tb = [], {'+':op.add, '-':op.sub, '*':op.mul, '/':lambda b,a:-(-b//a) if a*b<0 else b//a}
    #ops = tb.keys()
    for t in tokens:
        if not t in tb.keys(): s.append(int(t)) 
        else:
            i1 = s.pop(); i2 = s.pop()
            print(i2,t,i1,'=',tb[t](i2, i1))
            s.append(tb[t](i2, i1))
    return s[0] 

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(tokens)

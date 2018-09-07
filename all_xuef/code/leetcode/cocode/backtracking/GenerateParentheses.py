"""
22. Generate Parentheses

"""
def validate(p): # 校验括号的有效性
    stk = []
    for c in p:
        if c == '(':
            stk.append('(')
        elif c == ')':
            
            if not stk: return False
            if stk.pop() != '(': return False
    if stk: return False
    return True

def gen(p): # 生成有效的括号, 但结果中存在重复
    """
    :type p: List[str]--['(',')']
    :rtype: List[str]
    """
    sz = len(p)
    np = []
    for i in range(sz+1):
        tmp = p[:]
        tmp.insert(i,'(')
        for j in range(i+1, sz+2):
            tmp.insert(j, ')')
            if validate(tmp): np.append(tmp[:])
    return list(map(lambda x:''.join(x) ,np))
import functools as funct
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def helper(n):
        if n == 1: return ['()']
        lower = list(set(helper(n-1)))
        print(n-1,"-lower:",lower)
        cur = funct.reduce(lambda x, y: x+y, map(lambda x:gen(list(x)), lower))
        
        # 消除重复
        uniques = list(set(cur))
        print(n, "-cur:", uniques)
        return uniques
    return helper(n)
##p = ['(',')']
##print(validate(p))
##print(gen(p))
n=4
rs=generateParenthesis(n)     
print(rs)



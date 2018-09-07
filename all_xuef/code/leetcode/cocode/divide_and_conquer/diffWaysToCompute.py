
"""
241. Different Ways to Add Parentheses

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

"""
# numbers 是否是0-9? 不是! 输入也可以是 '11*12'
import operator as op
import re
def diffWaysToCompute(ipt):
    """
    :type input: str
    :rtype: List[int]
    """
    pass
tab = {'+':op.add, '-':op.sub, '*':op.mul}
def f(ipt, l, h):
    if l==h: return [int(ipt[l])]
    if l+2==h: return [tab[ipt[l+1]](int(ipt[l]),int(ipt[h]))]
    subs = [[[ipt[l:i],l,i-1],ipt[i],[ipt[i+1:h+1],i+1,h]] for i in range(l+1,h,2)]
    #print(subs)
    rs = [tab[sub[1]](j,k) for sub in subs \
          for j in f(ipt,sub[0][1],sub[0][2]) \
          for k in f(ipt,sub[2][1],sub[2][2])]
    print(rs)
    return rs

ipt = '2*3-4*5'
#ipt = '2-1-1'
#ipt = ''
#ipt = ['11','*','12']
to_lst = re.split(r"([\+\-\*])",ipt)
print(to_lst)
rs = f(to_lst,0,len(to_lst)-1)
print(rs)

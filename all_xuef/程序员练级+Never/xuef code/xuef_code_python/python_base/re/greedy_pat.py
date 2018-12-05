
"""
贪婪: 在满足整个大规则下尽可能多的匹配。
"""
import re
p=print
def text1():
    s="this is a number 123-456-789"
    pat=r"(.+)(\d+-\d+-\d+)" # pat=r"(.+?)(\d+-\d+-\d+)" 关闭+的贪婪模式
    ret=re.match(pat, s)

    p(ret.group(1))

def test2():
    s="haha1234qqqq"
    pat=r"haha(\d+?)"
    ret=re.match(pat,s)
    p(ret.group(1))

    pat=r"haha(\d+?)qqqq"
    ret=re.match(pat,s)
    p(ret.group(1))
    
test2()

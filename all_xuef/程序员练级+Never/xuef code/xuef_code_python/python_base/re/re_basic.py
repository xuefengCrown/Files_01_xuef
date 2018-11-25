
import re


p=print

#p('\n'.join([s for s in dir(re) if s.lstrip('_')[0].islower()]))
#p(help(re.match))
"""
match(pattern, string, flags=0)
    Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found.
"""

# pattern
"""
. 任意单字符(除了 \n)
[Hh]
[a-z]
*
-? (?前置一个字符可有可无)
\d === [0-9] === [0123456789]
\d{3,5}
[0-36-9]
[a-zA-Z]
\w === [a-zA-Z0-9_](支持中文字符)
\s
\S

\.

^
$

| or

() 提升优先级，分组
"""
rex = re.compile(r"[a-z]ello")
ret = rex.match("sello")

print(ret.group()) #与re exp匹配的部分


# 匹配字符串
s = """
hello,
world.
"""
rex = re.compile(r".*", re.S) # re.S 声明 . 也匹配 \n
ret = rex.match(s)
p(ret.group())

# 匹配变量名
var_names = ['a123', '___1', '1as', 'a1#', 'a-2']
rex4var = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*$")
for v in var_names:
    if rex4var.match(v):
        print("%-10s" % v, " >>>合法")
    else:
        print("%-10s" % v, " >>>不合法")

# 匹配163邮箱
# r"[a-zA-Z0-9_]{4,20}@163\.com$"
    

# 匹配html元素
html_content = "<h1>hello</h1>"
ret = re.match(r"<(\w+)>(.*)</\1>", html_content)
p(ret.group(2))


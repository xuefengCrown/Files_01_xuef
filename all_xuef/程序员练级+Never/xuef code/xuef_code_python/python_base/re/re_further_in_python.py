

# re.search
p = print
import re

#p(help(re.search))
"""
search(pattern, string, flags=0)
    Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.
"""
s = "阅读数 999"
ret = re.search(r"\d+", s) # search找到第一个后就返回
p(ret.group())

p20star = lambda :p("*"*20)

p20star()
#p(help(re.findall)) # Return a list of all non-overlapping matches in the string.
#p(help(re.sub)) #sub(pattern, repl, string, count=0, flags=0)

# 切割
p(help(re.split))

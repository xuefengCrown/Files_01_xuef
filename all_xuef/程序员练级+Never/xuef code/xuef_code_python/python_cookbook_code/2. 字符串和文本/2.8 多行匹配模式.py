
"""
你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。

"""
import re
p=print
##这个问题很典型的出现在当你用点(.)去匹配任意字符的时候，忘记了点(.)不能匹配换行符的事实。
##比如，假设你想试着去匹配C语言分割的注释：


comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'

text2 = '''/* this is a
... multiline comment */
'''


ret1=comment.findall(text1) #[' this is a comment ']
ret2=comment.findall(text2) #[]
p(ret1)
p(ret2)

#(?:.|\n) 的 ?:指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，
#而不能通过单独捕获或者编号的组)。
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
#comment2 = re.compile(r'/\*(.*?)\*/', flags=re.S)
ret3=comment2.findall(text1) #[' this is a comment ']
ret4=comment2.findall(text2) #[]
p(ret3)
p(ret4)





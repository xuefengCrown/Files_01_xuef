"""
你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。
而你想修改它变成查找最短的可能匹配。
"""
import re
p=print
# 这个问题一般出现在需要匹配一对分隔符之间的文本的时候(比如引号包含的字符串)。

## 模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。
str_pat_greedy = re.compile(r'"(.*)"') # 默认最长匹配模式
text1 = 'Computer says "no."'
ret1 = str_pat_greedy.findall(text1) #['no.']
p(ret1)

text2 = 'Computer says "no." Phone says "yes."'
ret2 = str_pat_greedy.findall(text2) #['no." Phone says "yes.']
p(ret2)

# 开启最短匹配模式
str_pat_short = re.compile(r'"(.*?)"')
ret3 = str_pat_short.findall(text2) #['no." Phone says "yes.']
p(ret3)


## 注意
#### 1. 在一个模式字符串中，点(.)匹配除了换行外的任何字符。

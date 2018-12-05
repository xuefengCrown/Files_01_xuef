
#### 配置环境
p=print
import re
####

p(help(re.search))
p(help(re.match))
p(help(re.findall))
# 它们具有一致的参数模式 (pattern, string, flags=0)

# 标志位 flags 的用处

##1. 为了在文本操作时忽略大小写， flags=re.IGNORECASE
#### 这也告诉我们: 我们可以使用关键字参数来为函数增加更多的控制和组合可能。




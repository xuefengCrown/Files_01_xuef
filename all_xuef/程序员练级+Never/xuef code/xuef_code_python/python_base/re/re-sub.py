"""
问题:
python2与3 的 print有着不同的语法:
    py2: print "hello"
    py3: print("hello")
而我们想实现py2<-->py3 的print语句的转换
"""
# lines 模拟文件
lines = [
    'print("[!!] Failed to listen on %s:%d" % (local_host,local_port))',
    'print("[!!] Check for other listening sockets or correct permissions.")',
    'print("[*] Listening on %s:%d" % (local_host,local_port))',
    'print("[==>] Received incoming connection from %s:%d" % (addr[0],addr[1]))'
]

import re
rex = re.compile(r"print\((.*)\)$")
for line in lines:
    subed = re.sub(rex, lambda match: "print " + match.group(1), line) # 动态替换
    print(subed)

"""
sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.
"""




# 对于任何事物，有几个重要问题:
# 0. 它是什么(第一属性 & 第二属性 本质vs表象)
# 1. 谓词判定(这个是不是它)
# 2. 它在哪儿
"""
对于文件，其本质是躺在磁盘某处的二进制数据。
至于文件名，创建时间，大小，权限等都只是第二属性。
"""

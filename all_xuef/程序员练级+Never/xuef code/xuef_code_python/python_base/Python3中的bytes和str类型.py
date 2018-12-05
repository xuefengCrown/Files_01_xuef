"""
Python 3最重要的新特性之一是对字符串和二进制数据流做了明确的区分。
文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。
Python 3不会以任意隐式的方式混用str和bytes，你不能拼接字符串和字节流，
也无法在字节流里搜索字符串（反之亦然），也不能将字符串传入参数为字节流的函数（反之亦然）。
"""
# bytes是一种比特流，它必须有一个编码方式，使得它变成有意义的比特流
## UTF-8编码规定英文字母系列用1个字节表示，汉字用3个字节表示等等。
## 因此，它兼容ASCII，可以解码早期的文档。
p=print

s="中文"
p(s)
b = bytes(s, encoding='utf-8') # b'\xe4\xb8\xad\xe6\x96\x87'
p(b)

# str to bytes
bytes(s, encoding = "utf8")

# bytes to str
str(b, encoding = "utf-8")

# an alternative method
# str to bytes
str.encode(s)

# bytes to str
bytes.decode(b)

"""
字符串类str里有一个encode()方法，它是从字符串向比特流的编码过程。
而bytes类型恰好有个decode()方法，它是从比特流向字符串解码的过程。
除此之外，我们查看Python源码会发现bytes和str拥有几乎一模一样的方法列表，
最大的区别就是encode和decode。

从实质上来说，字符串在磁盘上的保存形式也是01的组合，也需要编码解码。

1. 在将字符串存入磁盘和从磁盘读取字符串的过程中，Python自动地帮你完成了编码和解码的工作，
你不需要关心它的过程。

2. 使用bytes类型，实质上是告诉Python，不需要它帮你自动地完成编码和解码的工作，
而是用户自己手动进行，并指定编码格式。

3. Python已经严格区分了bytes和str两种数据类型，你不能在需要bytes类型参数的
时候使用str参数，反之亦然。这点在读写磁盘文件时容易碰到。
"""


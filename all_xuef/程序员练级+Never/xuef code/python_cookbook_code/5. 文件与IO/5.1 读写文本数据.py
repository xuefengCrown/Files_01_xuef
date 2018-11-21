
"""
文件读写的几个关键问题：
1. 使用with创建一个文件使用的上下文
2. 编码问题
3. 换行符的识别问题
"""


# 
def openfile():
    # Read the entire file as a single string
    """
        使用with, 给被使用到的文件创建了一个上下文环境
        with 控制块结束时，文件会自动关闭。
    """
    with open('somefile.txt', 'rt') as f:
        data = f.read()

    # Iterate over the lines of the file
    with open('somefile.txt', 'rt') as f:
        for line in f:
            # process line
            pass

    # Write chunks of text data
    with open('somefile.txt', 'wt') as f:
        f.write(text1)
        f.write(text2)

    # Redirected print statement
    with open('somefile.txt', 'wt') as f: # 如要追加文本，使用at模式
        print(line1, file=f)
        print(line2, file=f)

# 2. 编码问题
## 文件的读写操作默认使用系统编码，可以通过调用 sys.getdefaultencoding() 来得到。
import sys
encode = sys.getdefaultencoding()
print(encode)


# 3. 换行符的识别
"""
另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。
默认情况下，Python会以统一模式处理换行符。
这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。
类似的，在输出时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，
可以给 open() 函数传入参数 newline='' ，就像下面这样：

# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f:
    ...
"""



"""
问题
你想读写二进制文件，比如图片，声音文件等等。

使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据。
"""

def rwb():
    # Read the entire file as a single byte string
    with open('somefile.bin', 'rb') as f:
        data = f.read()

    # Write binary data to a file
    with open('somefile.bin', 'wb') as f:
        f.write(b'Hello World')


tstr = 'hello'
for c in tstr:
    print(c)

bstr = b'hello'
for b in bstr:
    print(b)

"""
如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作。比如：
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
"""




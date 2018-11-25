
"""
问题
你想将 print() 函数的输出重定向到一个文件中去。

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> 
"""
# 有一点要注意的就是文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错。

print(2018, 11, 21, sep='-')

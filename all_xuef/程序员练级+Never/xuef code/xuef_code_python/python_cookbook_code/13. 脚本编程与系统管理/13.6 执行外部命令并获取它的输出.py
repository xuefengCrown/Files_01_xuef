
# 你想执行一个外部命令并以Python字符串的形式获取执行结果。

## 使用 subprocess.check_output() 函数。

import subprocess as sp

p=print

## 这段代码执行一个指定的命令并将执行结果以一个字节字符串的形式返回。
##out_bytes=sp.check_output(['ipconfig'])

def exe_cmd(*args):
    out_bytes = None
    try:
        out_bytes=sp.check_output([*args]) # ['ping', 'www.baidu.com']
    except sp.CalledProcessError as e:
        print("execute cmd error")
    return out_bytes
    
##out_bytes = exe_cmd('ping', 'www.baidu.com')
out_bytes=exe_cmd('ipconfig')
p(out_bytes.decode('gbk'))

"""
使用 check_output() 函数是执行外部命令并获取其返回值的最简单方式。
但是，如果你需要对子进程做更复杂的交互，比如给它发送输入，你得采用另外一种方法。
这时候可直接使用 subprocess.Popen 类。
"""

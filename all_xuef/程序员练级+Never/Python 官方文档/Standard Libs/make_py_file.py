
import os

def make_py(fname=None, openit=False):
    """create file in current directory, and open it with IDLE3."""
    if fname is None:
        fname = input("py fname: ")
    fullname = fname + '.py'
    f = open(fullname, mode='w') # 'w' mode: if not exist, create it
    f.close()
    if openit:
        cmd = "C:\\python36\\pythonw.exe C:\\python36\\Lib\\idlelib\\idle.py " + "\"" + fullname + "\""
        os.system(cmd) # 处理文件名中包含的空格

def make_txt():
    fname = input("txt fname: ")
    cmd = "\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" " + "\"" + fname + "\""
    f = open(fname, mode='w') # 'w' mode: if not exist, create it
    f.close()
    # open with notepad++
    os.system(cmd + "& exit")
    
with open('contents.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        print(line)
        make_py(fname=line)

#make_txt()

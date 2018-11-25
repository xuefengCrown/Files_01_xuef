
import os

def make_py():
    """create file in current directory, and open it with IDLE3."""
    fname = input("py fname: ")
    fullname = fname + '.py'
    f = open(fullname, mode='w') # 'w' mode: if not exist, create it
    f.close()
    cmd = "C:\\python36\\pythonw.exe C:\\python36\\Lib\\idlelib\\idle.py " + "\"" + fullname + "\""
    os.system(cmd) # 处理文件名中包含的空格

def make_txt():
    fname = input("txt fname: ")
    cmd = "\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" " + "\"" + fname + "\""
    f = open(fname, mode='w') # 'w' mode: if not exist, create it
    f.close()
    # open with notepad++
    os.system(cmd + "& exit")
    
make_py()

#make_txt()

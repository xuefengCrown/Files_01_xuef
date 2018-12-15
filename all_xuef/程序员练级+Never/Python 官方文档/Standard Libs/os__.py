# 一个简单的 linux os指令cmd


# TODO
## 1. history (历史命令)
## 2. tab tab 命令补全

import os,sys, os.path
##from prompt_toolkit import prompt

def parse_cmd(cmd_str):
    idx = cmd_str.find(' ')
    if idx == -1: return cmd_str,
    return [cmd_str[:idx]] + cmd_str[idx+1:].split(',')
    #return cmd_str.split()

def exec_cd(params):
    os.chdir(params[0])
    
def exec_mkdir(params):
    # TODO: 批量mkdir,甚至支持 mkdir dir[a..z]
    [os.mkdir(p) for p in params]
    
def exec_pwd(params):
    res = os.getcwd()
    print(res)
    
def exec_ls(params):
    files = os.listdir(os.getcwd())
    [print("[d] ",f) for f in files if os.path.isdir(f)]
    [print("[--f] ",f) for f in files if os.path.isfile(f)]
    
def exec_mkf(params):
    for fname in params:
        f = open(fname, 'w')
        f.close()
def openit(exe_file_path, params):
    [os.system(exe_file_path + "\"" + f + "\"") for f in params]
    
def exec_py(params):
    exe_file_path = r"C:\python36\pythonw.exe C:\python36\Lib\idlelib\idle.py "
    openit(exe_file_path, params) # 处理文件名中包含的空格

# failed: 无法使用 Notepad 打开文件,不知道什么原因
def exec_edit(params):
    exe_file_path = '"C:\\Program Files (x86)\\Notepad++\\notepad++.exe" '
    openit(exe_file_path, params)
    
def dispatch(cmd, params):
    def exec_h(params):
        print("Support:")
        print("-"*40)
        [print("++ {cmd}:{info}".format(cmd=k,info=v[0])) for k,v in supports.items()]
    # TODO: 把supports放在一个文件中,利于修改和扩展
    supports = {'help': ("帮助", exec_h),
                'cd': ("cd dirname,进入目录",exec_cd),
                'mkdir': ("mkdir dirname,创建目录",exec_mkdir),
                'pwd': ("pwd,显示当前路径",exec_pwd),
                'ls': ("ls,显示目录下文件",exec_ls),
                'mkf': ("mkf fname,创建文件",exec_mkf),
                'edit': ("notepad", exec_edit),
                'py': ("py编辑器打开", exec_py)}
    
    return supports[cmd][1](params)

# C:\code_dxf\xuefgit\Files_01_xuef\all_xuef\程序员练级+Never\xuef code\xuef_code_python\Python高级编程
def exec():
    while True:
        try:
            cmd_str = input(">> ")
            
            cmd, *params = parse_cmd(cmd_str)
            res = dispatch(cmd, params)
            
        except KeyboardInterrupt as e:
            sys.exit()
        except Exception as e2:
            # TODO 提供详细的错误信息和指令提示
            print("Error")
            raise e2


p = print
if __name__ == '__main__':
    exec()
##print(os.getcwd())
##os.chdir(r'..')
##print(os.getcwd())
##print(os.listdir())

#p(os.environ['HOME']) #C:\Users\moveb

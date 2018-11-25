
import os
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量
listen=False
command=False
upload=False
execute=""
target=""
upload_destination=""
port=0

def usage():
    p=print
    p("BHP Net Tool")
    p("Usage: bhpnet.py -t target_host -p port")
    p("-l --listen    - listen on [host]:[port] for incoming connections")
    p("-e --execute=file_to_run    - execute the given file upon receiving a connection")
    p("-c --command     - initialize a command shell")
    p("-u --upload=destination    - upon receiving connection upload a file and write to [destination]")
    p()
    p()
    p("Examples")
    p("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    p("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    p("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    p("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 125")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu",\
                                   ["help","listen","execute","target","port"],"command","upload")
    except getopt.GetoptError as err:
        p(str(err))
        usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = True
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert(False, "Unhandled Option")



















            























        



















    

























    






















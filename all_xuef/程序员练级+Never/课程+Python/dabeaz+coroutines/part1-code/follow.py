# follow.py
#
# A generator that follows a log file like Unix 'tail -f'.
#
# Note: To see this example work, you need to apply to 
# an active server log file.  Run the program "logsim.py"
# in the background to simulate such a file.  This program
# will write entries to a file "access-log".

"""
fileObject.seek(offset[,whence])
参数
offset -- 偏移量，也就是代表需要移动偏移的字节数,注意是按照字节算的，
    字符编码存每个字符所占的字节长度不一样。
whence：可选，默认值为 0。表示要从哪个位置开始偏移；0代表从文件开头开始算起，
    1代表从当前位置开始算起，2代表从文件末尾算起。

"""
import time,pdb
def follow(thefile):
    #thefile.seek(-200,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         #pdb.set_trace()
         if not line:
             #time.sleep(0.1)    # Sleep briefly
             continue
         yield line

# Example use
if __name__ == '__main__':
    logfile = open("access-log", "rb")
    for line in follow(logfile):
        print (line)

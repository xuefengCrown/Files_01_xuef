
import ftplib


try:
    ftp = ftplib.FTP("hk801.pc51.com")
    # ftp = ftplib.FTP(host, user, passwd, acct, timeout)
    ftp.login("qinghuabeidacn517", "yinchengak47")
    print("login succ")
except:
    print("login failed")
    

# 下载网易云音乐 某页面的所有图片

#dl_pic.py 依序下载图片
import urllib.request
import urllib.parse

def download(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
    headers ={ 'User-Agent':user_agent}
    req = urllib.request.Request(url,headers = headers)
    # req.add_header("", "")
    response = urllib.request.urlopen(req)
    return response.read()

import os.path
from timeit import timeit
#http://music.163.com/song/media/outer/url?id=28557036.mp3
def main():
    n = 1
    with open(r".\pics\urls.txt", "rt") as urlf:
        for pic_url in urlf:
            pic_url = pic_url.rstrip("\n")
            jpg_file = download(pic_url)
            with open(os.path.join(".", "pics", str(n)+".jpg") , "wb") as f:
                n += 1
                f.write(jpg_file)
                print("download ", str(n)+".jpg")
            
if __name__ == '__main__':
    rtime = timeit(main, number=1)
    print(rtime, "s")#11.34 s


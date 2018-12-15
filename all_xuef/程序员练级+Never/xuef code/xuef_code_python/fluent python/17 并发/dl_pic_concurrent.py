# 下载网易云音乐 某页面的所有图片

#dl_pic_concurrent.py 并发下载图片
import urllib.request
import urllib.parse
from concurrent import futures

MAX_WORKERS = 20

def download(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
    headers ={ 'User-Agent':user_agent}
    req = urllib.request.Request(url,headers = headers)
    # req.add_header("", "")
    response = urllib.request.urlopen(req)
    return response.read()

import os.path
from timeit import timeit

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))# ➍
    with futures.ThreadPoolExecutor(workers) as executor: #➎
        res = executor.map(save_one, sorted(cc_list)) #➏
    return len(list(res)) 

#http://music.163.com/song/media/outer/url?id=28557036.mp3
def save_one(pic_url):
    try:
        jpg_file = download(pic_url)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        saved_name = pic_url.split("?")[0][-10:]
        with open(os.path.join(".", "pics", saved_name) , "wb") as f:
            f.write(jpg_file)
            print("download ", saved_name, end="\n")
        
def main():
    with open(r".\pics\urls.txt", "rt") as urlf:
        cc_list = [pic_url.rstrip("\n") for pic_url in urlf]
        download_many(cc_list)
        
if __name__ == '__main__':     
    rtime = timeit(main, number=1)
    print(rtime, "s")# 5.6s vs 11.34s


# python2 使用 urllib2.urlopen()
import urllib.request


def download(url):
    response = urllib.request.urlopen(url,timeout=10)   
    return response.info() #response.read(100)

url = "https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p09_define_decorators_as_classes.html"

try:
    print(download(url))
except URLError as e:
    print("error")

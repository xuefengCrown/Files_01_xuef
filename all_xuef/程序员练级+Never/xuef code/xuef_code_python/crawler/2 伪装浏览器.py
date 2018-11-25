# python2 使用 urllib2.urlopen()
import urllib.request


def download(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
    headers ={ 'User-Agent':user_agent}
    req = urllib.request.Request(url,headers = headers)
    # req.add_header("", "")
    response = urllib.request.urlopen(req)
    return response.info() #response.read(100)

url = "https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p09_define_decorators_as_classes.html"

try:
    print(download(url))
except URLError as e:
    print("error")

# 下载网易云音乐 某页面的所有图片


"""
先让我们看看浏览器处理过程中的每一个步骤：
1.处理HTML脚本，生成DOM树
2.处理CSS脚本，生成CSSOM树   （DOM和CSSOM是独立的数据结构）
3.将DOM树和CSSOM树合并为渲染树
4.对渲染树中的内容进行布局，计算每个节点的几何外观
5.将渲染树中的每个节点绘制到屏幕中
Headless Browser实际就是节约了第4,5步的时间。

3年前，无头浏览器 PhantomJS 已经如火如荼出现了，紧跟着 NightmareJS 也成为一名巨星。
无头浏览器带来巨大便利性：页面爬虫、自动化测试、WebAutomation...用过PhantomJS的都知道，
它的环境是运行在一个封闭的沙盒里面，在环境内外完全不可通信，包括API、变量、全局方法调用等。
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import urllib.request
import urllib.parse

p=print

def get_srcs(url="https://music.163.com/#/song?id=28557036"):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # http://music.163.com/song/media/outer/url?id=28557036
    driver.get(url)

    ##WebDriverWait(driver, 10)
    ##driver.implicitly_wait(20)
    ##p('\n'.join([m for m in dir(driver) if not m.startswith('_')]))

    driver.switch_to.frame("contentFrame")
    # view 截图
    driver.save_screenshot('screen.png')

    p("done...")
    ##p(help(driver.execute_async_script))
    ##html_content=driver.page_source

    imgs = driver.find_elements_by_tag_name('img')
    ##p(type(imgs))
    srcs = [e.get_attribute("src") for e in imgs]

    ##import sys
    ##non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    ##p(html_content.translate(non_bmp_map))

    import time
    time.sleep(2)
    driver.quit()

    return [src for src in srcs if not src.endswith(".png")]

def download(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
    headers ={ 'User-Agent':user_agent}
    req = urllib.request.Request(url,headers = headers)
    # req.add_header("", "")
    response = urllib.request.urlopen(req)
    return response.read() # 响应的报头

# http://p2.music.126.net/vvep8oWbYOhpWchNu4C8qg==/6022025185715205.jpg?param=130y130
def chg_pic_size(url, width, height):
    parts = url.split('?')
    return "{0}?param={1}y{2}".format(parts[0], width, height)

#http://music.163.com/song/media/outer/url?id=28557036.mp3
def main():
    srcs = get_srcs("https://music.163.com/#/playlist?id=459944247")
    
##    n = 1
##    for src in srcs:
##        new_src = chg_pic_size(src, 1000, 1000)
##        p(new_src)
##        jpg_file = download(new_src)
##        with open(str(n)+".jpg", "wb") as f:
##            n += 1
##            f.write(jpg_file)
            
if __name__ == '__main__':
    main()
##with open("music.txt", 'wt') as f:
##browser = webdriver.Chrome()
##browser.get('http://www.baidu.com/')



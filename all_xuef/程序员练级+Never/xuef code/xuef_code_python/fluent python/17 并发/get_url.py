# save网易云音乐 某页面的所有图片的url,为后序的download做准备

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import urllib.request
import urllib.parse

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

    print("done...")
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

# http://p2.music.126.net/vvep8oWbYOhpWchNu4C8qg==/6022025185715205.jpg?param=130y130
def chg_pic_size(url, width, height):
    parts = url.split('?')
    return "{0}?param={1}y{2}".format(parts[0], width, height)

#http://music.163.com/song/media/outer/url?id=28557036.mp3
def main():
    srcs = get_srcs("https://music.163.com/#/playlist?id=459944247")
    with open(r".\pics\urls.txt", "wt") as f:
        for src in srcs:
            new_src = chg_pic_size(src, 1000, 1000)+"\n"
            f.write(new_src)
            
if __name__ == '__main__':
    main()
##with open("music.txt", 'wt') as f:
##browser = webdriver.Chrome()
##browser.get('http://www.baidu.com/')



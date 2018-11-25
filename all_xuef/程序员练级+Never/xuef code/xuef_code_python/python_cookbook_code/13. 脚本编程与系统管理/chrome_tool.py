import webbrowser as wb

tabs = {
    'bd': ("baidu", "https://www.baidu.com"),
    'g' : ("google", "www.google.com"),
    'bili': ("bilibili", "https://www.bilibili.com"),
    'rm': ("runningman", "http://www.runningmanzx.com/shipin/"),
    'pc': ("python3-cookbook", "https://python3-cookbook.readthedocs.io/zh_CN/latest"),
    'e' : ("exit", "https://blog.csdn.net/str999_cn/article/details/78879547")
    }
def open_url():
    p = print
    while 1:
        # url 缩写表
        p("*"*10,"url-abbr", "*"*10)
        for short_name, vals in tabs.items():
            p("   %s<-->%s " % (vals[0],short_name))
        p("*"*10,"url-abbr", "*"*10)
        
        short_name = input("site-name(abbr): ")
        if short_name == 'e': break
        wb.open(tabs[short_name][1])
if __name__ == '__main__':
    open_url()

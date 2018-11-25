

class MiniOS:
    def __init__(self, name):
        self.name=name # os name 
        self.apps=[] #安装的软件
    def __repr__(self):
        return "%s 安装的软件 %s" % (self.name, str(self.apps))

    def install_app(self, app):
        if app.name in self.apps:
            print("%s 已安装".format(app.name))
        else:
            app.install()
            self.apps.append(app.name)
            print(app.name, "install finished...")

class App(object):
    def __init__(self, name, version, desc):
        self.name=name
        self.version=version
        self.desc=desc

    def __str__(self):
        return "%s 当前版本是 %s - %s" % (self.name, self.version, self.desc)

    def install(self):
        print("将 %s [%s] 的执行程序复制到程序目录..." % (self.name, self.version))

class PyCharm(App):
    pass
class Chrome(App):
    def install(self):
        print("正在解压程序...")
        super().install()


linux = MiniOS("linux")
chrome1 = Chrome("chrome", "v1.1", "a great browser.")

linux.install_app(chrome1)

















        

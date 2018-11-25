

def withcheck(f):
    def inner():
        print("正在验证权限...")
        f()
    return inner

def dosth():
    print("do something...")

dosth = withcheck(dosth)
dosth()

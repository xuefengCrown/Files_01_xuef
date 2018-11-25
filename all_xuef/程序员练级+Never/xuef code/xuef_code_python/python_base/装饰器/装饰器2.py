

def withcheck(f):
    def inner():
        print("正在验证权限...")
        f()
    return inner

# dosth = withcheck(dosth)
@withcheck
def dosth():
    print("do something...")

dosth()

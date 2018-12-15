
# 代理装饰器使用一个全局机制来标记和注册函数。
# 例如，一个根据当前用户保护代码访问的安全层可以使用一个集中检查器和相关的可调用
# 对象要求的权限来实现。

class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(func):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return func(*args, **kw)
        return __protect
    return _protect

# 这种模式常应用于 web框架,用来定义针对可发布类的安全性。
# 例如，Django提供装饰器来保障函数访问的安全。

adm = User(('admin', 'user'))
regul = User(('user',))

class MySecrets():
    @protect('admin')
    def waffle_recipe(self):
        print("use tons of butter!")

secret = MySecrets()
user = adm
secret.waffle_recipe()

user = regul
secret.waffle_recipe()














    

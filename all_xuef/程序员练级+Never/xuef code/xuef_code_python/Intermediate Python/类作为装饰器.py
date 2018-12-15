
"""
场景:
当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。
比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，
同时也保留日志，留个记录。

"""
from functools import wraps

class Logit(object):
    def __init__(self, logfile="out.log"):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 打日志
            with open(self.logfile, "at") as f:
                print("{func} was called...".format(func=func.__name__), file=f)

            # 其他处理    
            self.notify()
            
            return func(*args, **kwargs)
        return wrapper
    
    def notify(self):
        pass


class Logit_and_Email(Logit):
    """
    一个Logit的实现版本，可以在函数调用时发送email给管理员
    """
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        super(Logit_and_Email, self).__init__(*args, **kwargs)
        self.email = email
        

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        print("send email to {email}".format(email=self.email))
        pass           


@Logit_and_Email()
def sq(x):
    print(x*x)
    
sq(5)

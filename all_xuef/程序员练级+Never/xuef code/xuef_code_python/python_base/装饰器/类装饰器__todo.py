from functools import wraps

class logit:
    def __init__(self, logfile='out.log'):
        self.logfile = logfile
        
    @wraps(func)
    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            log_str = func.__name__ + "is called"
            print(log_str)
            with open(self.logfile, 'wa') as f:
                f.write(log_str + '\n')
            # send a msg
            self.notify()
            return func(*args, **kwargs)
        return wrapped_func
    def notify(self):
        pass


class email_logit(logit):
    """
    一个logit的实现版本，可以在函数调用时发送email给管理员
    """
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        print("send an email")












    


"""
问题
你想通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化。
"""

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, y, m, d):
        self.day = d
        self.month = m
        self.year = y
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2018, 11, 21)

print(format(d))

print(format(d, 'mdy'))















    
        






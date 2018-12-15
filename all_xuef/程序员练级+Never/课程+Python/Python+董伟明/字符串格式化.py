
# 设置全局变量
d={'p':print}

globals().update(d)

print('\n'.join(globals()))


#format格式化字符串更加强大
## 使用命名参数
p("{k}={v}".format(k='one', v="1"))

## 左中右
p("[{0:<10}], [{0:^10}], [{0:*>10}]".format('a'))

## 成员
import sys
p("{0.platform}".format(sys))

## 字典
p("{0[a]}".format(dict(a=10, b=20)))

## 列表
p("{0[5]}".format(range(10)))

## ??
p("{0!r:20}".format("hello"))

p("{0!s:20}".format("hello"))

##
import datetime
p("Today is: {0:%a %b %d %H:%M:%S %Y}".format(datetime.now))
















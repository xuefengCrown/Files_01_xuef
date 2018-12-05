
"""
re.match
re.search
re.sub
re.findall
"""

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
p=print

datepat = re.compile(r'\d+/\d+/\d+')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
all_match = datepat.findall(text) #['11/27/2012', '3/13/2013']

p(all_match)

# 在定义正则式的时候，通常会利用括号去捕获分组。比如：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

#需要注意的是 match() 方法仅仅检查字符串的开始部分。
#返回与模式匹配的部分。
m = datepat.match('11/27/2012')
p(m.group(0))
p(m.group(1))
p(m.group(2))
p(m.group(3))
p(m.groups())

month, day, year = m.groups()

datepat.findall(text) #[('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替，比如：
for m in datepat.finditer(text):
    print(m.groups())

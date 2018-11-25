
"""
场景：
你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。

"""
def drop_first_last(grades):
    def avg(numList):
        return sum(numList)/len(numList)
    first, *middle, last = grades
    return avg(middle)

grades = [99, 80, 88, 76]

avg = drop_first_last(grades)
print(avg)


# 解压出的 phone_numbers 变量永远都是列表类型
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record 


#星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

"""
在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。
比如，如果你有一个列表， 你可以很容易的将它分割成前后两部分：
"""
items = [1, 10, 7, 4, 5, 9]
car, *cdr = items
print("car=", car, "cdr=", cdr)

# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法
def sam(items):
    car, *cdr = items
    return car + sam(cdr) if cdr else car # 注意python中的false值有哪些
"""
>>> bool([])
False
>>> bool(0)
False
>>> bool(())
False
>>> bool({})
False
>>> bool(None)
False
>>> bool("")
False
"""
# 然后，由于语言层面的限制，递归并不是 Python 擅长的。
assert(sum(items) == sam(items))
print(sam(items))


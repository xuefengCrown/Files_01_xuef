"""
我们追求的目标:
清晰易读, 高效简洁
"""
#1. Pythnic
## 使用列表推导式来代替 map/filter

## 生成器作为数据接口, 尤其是数据量很大时

## 使用zip平行遍历多个迭代器(itertools.zip_longest)

#2. 函数
""" Python程序员首先接触的代码组织工具，就是函数
函数还为复用和重构提供了契机

目标:
1. 彰显函数的功能, 清晰!
2. 减少杂乱的语句并阐明调用者的意图
3. 有力地防止程序里出现难于查找的bug
"""

## 14 尽量用异常来表示特殊情况，而不要返回 None

## 15 了解如何在闭包里使用外围作用域中的变量
#### 15.1 元组的比较规则
#### 15.2 nonlocal的唯一限制是，它不能延伸到模块级别，这是防止它污染全局作用域。
####    不要滥用nonlocal

##start code-15
#对于存在于group中的元素，有较高的优先级
def sort_priority(vals, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0,x) # 对x进行加权
        else:
            return (1,x)
        
    vals.sort(key=helper)    
    return found

vals = [8,3,1,2,5,4,7,6]
group = [2,3,5,7]
#sort_priority(vals, group)
#print(vals)

# 重写sort_priority，以避免sort_priority
class Sorter():
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in group:
            self.found = True
            return (0,x) # 对x进行加权
        else:
            return (1,x)

sorter = Sorter(group)
vals.sort(key=sorter)
print(vals, sorter.found)
##end code-15


## 16 考虑用生成器来改写直接返回列表的函数
#### 这样就不需要包含与 result列表交互的那些代码(比如收集元素)


## 19 用关键字参数来表达可选的行为
#### 位置参数必须出现在关键字参数之前


## 20 用None和文档字符串来描述具有动态默认值的参数
#### 参数的默认值，会在每个模块加载进来的时候求出，而很多模块是在程序启动时加载的。
#### 如果参数的实际默认值类型是可变类型，那就一定要记得用None作为形式上的默认值。

































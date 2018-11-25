"""
类(Person,Province)本就是个模板。模板当然是对象。它属于模板(class)类型
人模板(Person), 省模板(Province)
"""
# 解释器在遇到 class A 时会做什么?

# 类是对象意味着我们可将它看作一个实体，进而可以对它进行审视和操作，施加影响。

## 你可以在运行时创建它
class Province():
    country = "China"
    def __init__(self, name):
        self.name = name


print(type(10)) # <class 'int'> 意味着10是用int类(型)创建出来的对象
p=Province("zhejiang")
print(type(p)) #<class '__main__.Province'>
# 意味着 p 是用Province类创建出来的对象
print(type(Province)) #<class 'type'>
# 意味着 Province是用 class 类创建出来的对象

# 可以使用 type 创建类(class类的对象)
#type(类名, 由父类名称组成的元组,包括属性的字典)





















#1. python没有 "块级作用域"
if 1==1:
    name0 = "xuef"
print(name0)

##在Java/C 中，执行上面的代码会提示name没有定义，而在Python中可以执行成功，
##这是因为在Python中是没有块级作用域的，代码块里的变量，外部可以调用，所以可运行成功；


#2. 有局部作用域
def func():
    local = "haha"
func()
#print(local) # not defined


#终极版作用域
name = "lzl" 
def f1():
    print(name)
def f2():
    name = "eric"
    f1()
f2()

#5、新浪面试题
li = [lambda :x for x in range(10)]
##判断下li的类型？li里面的元素为什么类型？
#记住：函数在没有执行前，内部代码不执行

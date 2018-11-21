

# 匿名函数
(lambda s: print(s))("hello,world")

# 变长参数
def test_args(*tupleArg, **dictArg):
    print(tupleArg, dictArg)


argList = ["str1","str2"]
argDict = {"name":"Tom", "age":22}

test_args(*argList, **argDict)

"""
"hello", "world" 会被打包到一个元祖中, 于是tupleArg = ("hello", "world")
name="xuef", age=28 会被dict 一下, 于是 dictArg = {name="xuef", age=28}
"""
test_args("hello", "world", name="xuef", age=28)

def mysum(*operands):
    if len(operands) == 0:
        return 0
    else:
        return operands[-1] + mysum(*operands[:-1]) # *:解包,[1,2,3]--> 1,2,3

print(mysum(1,2,3,4,5))






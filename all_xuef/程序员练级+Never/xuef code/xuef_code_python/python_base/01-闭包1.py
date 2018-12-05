"""
闭包的本质是: 轻量级封装数据和代码的容器
(而对象则是重量级容器，它提供了更丰富的功能)
"""


def test(number):

    print("--1--")

    def test_in(number2):
        print("--2--")
        print(number+number2)

    print("--3--")
    return test_in


ret = test(100)
print("-"*30)
ret(1)
ret(100)
ret(200)

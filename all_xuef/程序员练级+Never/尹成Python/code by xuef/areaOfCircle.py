
"""
S = pi*R*R
TODO：
1. 对不合法输入(如10a) 的处理
2. 封装程序
"""
pi = 3.1415
R = input("请输入圆的半径:")
R_val = eval(R) # str --> int
S = pi * R_val * R_val

print("S=", S)

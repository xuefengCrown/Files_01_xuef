

"""
我至今遇到的把python讲的最清楚的课程就属 cs61b了
"""

# 闭包

def line_conf(a, b):
    def line(x): # 注意 def 背后发生了什么(解释器层面)
        return a*x + b
    return line

line1 = line_conf(1, 1) # 定义直线 y = 1*x + 1
line2 = line_conf(2, 3) # 定义直线 y = 2*x + 3

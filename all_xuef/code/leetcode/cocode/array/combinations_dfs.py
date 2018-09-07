
##import Queue
def combinations(n, k):
    if k == 0: return [[]]

    # res, cbn 这里应该是全局作用域的, 如何实现?
    # 1. 类的实例变量?
    # 2. global 声明(不知道为什么不起作用)
    # 3. 作为函数参数传递
    res = []
    cbn = []

    """
    dfs的框架, 但是这里的解空间树是哪个, 如何构造, 我困惑了好久;
    """
    # r, c 传递的是引用
    def dfs(n, k, start, r, c):
        # 约束条件?
        if len(cbn) == k:
            res.append(cbn[:]) # 知道什么时候需要一个新的列表
        else:
            # 间接构造了解空间树?
            for i in range(start, n+1): # 困扰我的扩展节点
                cbn.append(i)
                dfs(n, k, i+1, r, c)
                cbn.pop()
                i += 1
                
    dfs(n, k, 1, res, cbn)
    return res
    
print(combinations(5,3))



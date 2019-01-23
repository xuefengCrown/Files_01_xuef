
#模式匹配
"""
前面的章节介绍了代数数据类型的定义方法，本节将说明怎样去处理这些类型的值。

对于某个类型的值来说，应该可以做到以下两点：

如果这个类型有一个以上的值构造器，那么应该可以知道，这个值是由哪个构造器创建的。
如果一个值构造器包含不同的成分，那么应该有办法提取这些成分。
对于以上两个问题， Haskell 有一个简单且有效的解决方式，那就是类型匹配。
"""

#模式匹配允许我们查看值的内部，并将值所包含的数据绑定到变量上。

##以下是一个对 Bool 类型值进行模式匹配的例子，它的作用和 not 函数一样：
"""
-- file: myNot.hs
myNot True = False
myNot False = True
"""

#以下是一个复杂一点的例子，这个函数计算出列表所有元素之和：
"""
-- file:: ch03/sumList.hs
sumList (x:xs) = x + sumList xs
sumList []  = 0
"""
#需要说明的一点是，在 Haskell 里，列表 [1, 2] 实际上只是 (1:(2:[])) 的一种简单的表示方式，
#其中 (:) 用于构造列表
"""
因此，当需要对一个列表进行匹配时，也可以使用 (:) 操作符，只不过这次不是用来构造列表，而是用来分解列表。

作为例子，考虑求值 sumList [1, 2] 时会发生什么：首先， [1, 2] 尝试对第一个等式的模式 (x:xs) 进行匹配，
结果是模式匹配成功，并将 x 绑定为 1 ， xs 绑定为 [2] 。

"""

"""
让我们稍微慢下探索新特性的脚步，花些时间，了解构造一个值、和对这个值进行模式匹配之间的关系。

我们通过应用值构造器来构建值：表达式 Book 9 "Close Calls" ["John Long"] 应用 Book 构造器到值
9 、 "Close Calls" 和 ["John Long"] 上面，从而产生一个新的 BookInfo 类型的值。

另一方面，当对 Book 构造器进行模式匹配时，我们逆转（reverse）它的构造过程：
首先，检查这个值是否由 Book 构造器生成 —— 如果是的话，
那么就对这个值进行探查（inspect），并取出创建这个值时，提供给构造器的各个值。
"""

#我们在定义一种数据类型的同时，就可以定义好每个成分的访问器。
"""
-- file: ch03/BookStore.hs
data Customer = Customer {
      customerID      :: CustomerID
    , customerName    :: String
    , customerAddress :: Address
    } deriving (Show)
"""


#递归类型
##列表这种常见的类型就是递归的：即它用自己来定义自己。
"""
-- file: ch03/ListADT.hs
data List a = Cons a (List a)
            | Nil
              deriving (Show)
"""

#定义一个二叉树类型。
"""
-- file: ch03/Tree.hs
data Tree a = Node a (Tree a) (Tree a)
            | Empty
              deriving (Show)
"""



##定义局部函数 plural
"""
-- file: ch03/LocalFunction.hs
pluralise :: String -> [Int] -> [String]
pluralise word counts = map plural counts
    where plural 0 = "no " ++ word ++ "s"
          plural 1 = "one " ++ word
          plural n = show n ++ " " ++ word ++ "s"
"""






















#初学 Haskell 的人需要迈过两个难关：

##首先，我们需要将自己的编程观念从命令式语言转换到函数式语言上面来。
##其次，我们需要熟悉 Haskell 的标准库。和其他语言一样，函数库可以像杠杆那样，
##极大地提升我们解决问题的能力。因为 Haskell 是一门层次非常高的语言，而 Haskell
##的标准库也趋向于处理高层次的抽象，因此对 Haskell 标准库的学习也稍微更难一些，
##但这些努力最终都会物有所值。


"""
-- file: ch04/square.hs

square :: [Double] -> [Double]

square (x:xs) = x*x : square xs
square []     = []
"""
#square 函数包含两个模式匹配等式。


#列表映射
##以下是使用 map 重写的 square 和 upperCase 函数：
"""
-- file: ch04/rewrite_by_map.hs

import Data.Char (toUpper)

square2 xs = map squareOne xs
    where squareOne x = x * x

upperCase2 xs = map toUpper xs
"""



"""
-- file: ch03/BookStore.hs
type CardHolder = String
type CardNumber = String
type Address = [String]
data BillingInfo = CreditCard CardNumber CardHolder Address
                 | CashOnDelivery
                 | Invoice CustomerID
                   deriving (Show)
"""

#其他语言里类似代数数据类型的东西
"""
当只有一个值构造器时，代数数据类型和元组很相似：它将一系列相关的值打包成一个复合值。
这种做法相当于 C 和 C++ 里的 struct ，而代数数据类型的成分则相当于 struct 里的域。

"""


"""
C 和 C++ 里的 enum 通常用于表示一系列符号值排列。代数数据类型里面也有相似的东西，一般称之为枚举类型。

以下是一个 enum 例子：

enum roygbiv {
    red,
    orange,
    yellow,
    green,
    blue,
    indigo,
    violet,
};

以下是等价的 Haskell 代码：

-- file: ch03/Roygbiv.hs
data Roygbiv = Red
             | Orange
             | Yellow
             | Green
             | Blue
             | Indigo
             | Violet
               deriving (Eq, Show)
"""
#enum 的问题是，它使用整数值去代表元素：在一些接受 enum 的场景里，可以
#将整数传进去，C 编译器会自动进行类型转换。

#另一方面，在 Haskell 里就没有这样的问题。比如说，不可能使用 Roygbiv 里的某个值来代替 Int 值



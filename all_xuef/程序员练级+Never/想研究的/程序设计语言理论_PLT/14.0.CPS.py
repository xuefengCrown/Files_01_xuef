

"""
(letrec ((f (lambda (x) (cons 'a x)))
         (g (lambda (x) (cons 'b (f x))))
         (h (lambda (x) (g (cons 'c x)))))
  (cons 'd (h '())))


上面的程序可以重新写成：

(letrec ((f (lambda (x k) (k (cons 'a x))))
         (g (lambda (x k)
              (f x (lambda (v) (k (cons 'b v))))))
         (h (lambda (x k) (g (cons 'c x) k))))
  (h '() (lambda (v) (cons 'd v))))
  
这里每个函数多了一个参数 k， 表示一个 continuation。




"""
#
"""
我们其实做了很多无用功，我们首先用一个展开过程访问了所有的叶 结点，而在比较时，
到第3个叶结点(c和d)就发生了不匹配，如果能 不访问之后的叶子就好了。

现在我们有一个好主意：能不能在对两棵树进行遍历的同时就两两比 较叶子是否相同？
一旦发现途中有一对叶子不同，我们马上就可以断 定这两棵树不匹配。

这么自然的想法，却不容易用普通的控制结构实现，在遇到一个叶子 时，你如何能够跳出遍历的过程，
把这个叶子传递给一个比较过程？比较之后，你如何回到刚才遍历的路径中？

"""










"""
int i = add(5, 10);
int j = square(i);

函数 add 在其被调用的位置将结果 15 赋给了 i，接下来 i 的值被用来调用 square。
注意所有的惰性求值编译器都不能调整这几行代码因为第二行依赖着第一行的成功求值。
下面用 continuation 风格又称 CPS（Continuation Programming Style）来重写这段代码，
这里函数 add 会将结果返回到 square 而不是原来的调用函数。

int j = add(5, 10, square);
"""
## add需要被转换???????

"""
因此，这里转化的核心就是把每个单参数函数 f  转换成具有额外参数的函数。这个额外的参
数就是continuation，代表了其余的计算。Continuation本身也是单参数的函数。这个参数的
输入是 f  本来的返回值，后续计算本来需要使用这个返回值继续。转换后 f  将不再返回值，
而是将原来的返回值传递给它的continuation。

我们的CPS表示法会将每个表达式转变成单参数的函数，参数就是continuation。转换后的表
达式最终要么提供值调用continuation，要么将continuation传递给其他表达式，归纳地说，其
他表达式也遵从这个不变量关系，因此最终continuation会被提供某个值。所以说，所有的
CPS输出看起来都类似于 (lambda (k) ...).
"""


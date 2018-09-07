

## 8.1 符号名 (Symbol Names)



## 8.2 属性列表 (Property Lists)

在 Common Lisp 里，每个符号都有一个属性列表（property-list）或称为 `plist` 。函数 `get` 接受符号及任何类型的键值，然后返回在符号的属性列表中，与键值相关的数值：

```
> (get 'alizarin 'color)
NIL
```

它使用 `eql` 来比较各个键。若某个特定的属性没有找到时， `get` 返回 `nil` 。

要将值与键关联起来时，你可以使用 `setf` 及 `get` :

```
> (setf (get 'alizarin 'color) 'red)
RED
> (get 'alizarin 'color)
RED
```

现在符号 `alizarin` 的 `color` 属性是 `red` 。



## 8.3 符号很不简单 (Symbols Are Big)

当我们输入名字时，符号就被悄悄地创建出来了，而当它们被显示时，我们只看的到符号的名字。某些情况下，把符号想成是表面所见的东西就好，别想太多。但有时候符号不像看起来那么简单。

从我们如何使用和检查符号的方式来看，符号像是整数那样的小对象。而符号实际上确实是一个对象，差不多像是由 `defstruct` 定义的那种结构。符号可以有名字、 主包（home package）、作为变量的值、作为函数的值以及带有一个属性列表。图 8.1 演示了符号在内部是如何表示的。

很少有程序会使用很多符号，以致于值得用其它的东西来代替符号以节省空间。但需要记住的是，符号是实际的对象，不仅是名字而已。当两个变量设成相同的符号时，与两个变量设成相同列表一样：两个变量的指针都指向同样的对象。



## 8.5 多重包 (Multiple Packages)

举例来说，假设一个程序分为两个包， `math` 与 `disp` 。如果符号 `fft` 被 `math` 包导出，则 `disp` 包里可以用 `math:fft` 来参照它。在 `math` 包里，可以只用 `fft` 来参照。

下面是你可能会放在文件最上方，包含独立包的代码：

```
(defpackage "MY-APPLICATION"
            (:use "COMMON-LISP" "MY-UTILITIES")
            (:nicknames "APP")
            (:export "WIN" "LOSE" "DRAW"))

(in-package my-application)

```

`defpackage` 定义一个新的包叫做 `my-application` [[1\]](http://acl.readthedocs.io/en/latest/zhCN/ch8-cn.html#id4) 它使用了其他两个包， `common-lisp` 与 `my-utilities` ，这代表着可以不需要用包修饰符（package qualifiers）来存取这些包所导出的符号。许多包都使用了 `common-lisp` 包 ── 因为你不会想给 Lisp 自带的操作符与变量再加上修饰符。



`my-application` 包本身只输出三个符号: `WIN` 、 `LOSE` 以及 `DRAW` 。由于调用 `defpackage` 给了 `my-application` 一个匿称 `app` ，则别的包可以这样引用到这些符号，比如 `app:win` 。

`defpackage` 伴随着一个 `in-package` ，确保当前包是 `my-application` 。所有其它未修饰的符号会被扣押至 `my-application` ── 除非之后有别的 `in-package` 出现。当一个文件被载入时，当前的包总是被重置成载入之前的值。



## 8.6 关键字 (Keywords)

在 `keyword` 包的符号 (称为关键字)有两个独特的性质：它们总是对自己求值，以及可以在任何地方引用它们，如 `:x` 而不是 `keyword:x`。我们首次在 44 页 (译注: 3.10 小节）介绍关键字参数时， `(member '(a) '((a) (z)) test: #'equal)` 比 `(member '(a)'((a) (z)) :test #'equal)` 读起来更自然。现在我们知道为什么第二个较别扭的形式才是对的。 `test` 前的冒号字首，是关键字的识别符。

为什么使用关键字而不用一般的符号？因为关键字在哪都可以存取。一个函数接受符号作为实参，应该要写成预期关键字的函数。举例来说，这个函数可以安全地在任何包里调用:

```
(defun noise (animal)
  (case animal
    (:dog :woof)
    (:cat :meow)
    (:pig :oink)))
```

但如果是用一般符号写成的话，它只在被定义的包内正常工作，除非关键字也被导出了。

## 8.7 符号与变量 (Symbols and Variables)

Lisp 有一件可能会使你困惑的事情是，符号与变量的从两个非常不同的层面互相关联。当符号是特别变量（special variable）的名字时，变量的值存在符号的 value 栏位（图 8.1）。 `symbol-value` 函数引用到那个栏位，所以在符号与特殊变量的值之间，有直接的连接关系。

而对于词法变量（lexical variables）来说，事情就完全不一样了。一个作为词法变量的符号只不过是个占位符（placeholder）。编译器会将其转为一个寄存器（register）或内存位置的引用位址。在最后编译出来的代码中，我们无法追踪这个符号 (除非它被保存在调试器「debugger」的某个地方)。因此符号与词法变量的值之间是没有连接的；只要一有值，符号就消失了。


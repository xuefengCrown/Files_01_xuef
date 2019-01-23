

# 查看帮助
"""
查看 LISP 函数说明： C-h f ---> Describe function: 输入函数名
查看 LISP 变量说明： C-h v ---> Describe variable: 输入变量名

[
    例如，要查看 concat 的函数说明，可以按 Ctrl+h f,
    回显区会显示 Describe function: 在冒号后输入 concat 即可。
]
"""

# 执行一段代码
"""
LISP 表达式求值： 将光标移到LISP表达式的右括号外，按 C-x C-e

安装自定义的 LISP 函数：
(1) 在函数定义后的右括号外执行 C-x C-e 即可[只能供本次使用，下次打开时又要安装]。
(2) 写在一个文件里，然后在 .emacs 中加载。

"""

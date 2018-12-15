
"""
诸如python的"foo = {foo}!".format(foo=17)这样的字符串格式化函数是一种小语言的典型例子，
这种语言被用来从字符串字面量和要被插入的数据创建文本。
模板拓展了这个想法，包含了条件和循环结构，不同之处只是拓展的程度。

这些文件之所以被称为模板是因为它们被用来产生许多具有相似结构与不同细节的页面。

模板引擎的任务是翻译模板，用动态数据替换其中的动态片段。

Rendering the template specifically involves:
    Managing the dynamic context, the source of the data
    Executing the logic elements
    Implementing dot access and filter execution
    
The question of what to pass from the parsing phase to the rendering phase is key.
What does parsing produce that can be rendered?
There are two main options; we'll call them interpretation and compilation,
using the terms loosely from other language implementations.

"""
# 值得进一步学习的
## 解释器模型
## 编译模型
## 代码生成的通用技术

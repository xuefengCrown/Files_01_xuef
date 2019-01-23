
##我们直观上认为是单词的东西，实际只需要用三类规则就可以形式地描述清楚：
##拼接、选择和星号(任意次的重复)。
#基于这三种规则定义出的任何字符串集合都称为正则集。

##为描述直观认为是语法的东西的其他大部分内容，我们还需要加上一种递归(从更简单的结构创建起同样的结构)
#如果一个字符串集合可以通过加入递归后的规则形式地定义，那么就称它是一个上下文无关语言(CFL)
#它由上下文无关文法(CFG)定义，由语法分析器识别。


#上下文无关文法
## 描述嵌套结构
"""
expr --> id | number | - expr | ( expr )
         | expr op expr
op --> + | - | * | /

As an example, we can use our grammar for expressions to generate the string:
'slope * x + intercept'
expr ⇒ expr op expr
     ⇒ expr op id
     ⇒ expr + id
     ⇒ expr op expr + id
     ⇒ expr op id + id
     ⇒ expr * id + id
     ⇒ id   *   id     +    id
     (slope)     (x)    (intercept)
"""
# 不断替换非终结符(位于左部的)
# 语法分析树






















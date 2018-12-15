
# 模板引擎的任务是翻译模板，用动态数据替换其中的动态片段。

"""
顺便一提，模板引擎并不是针对HTML，它能用来产生任何文本结果。
比如，它们也用来生成纯文本电子邮件消息。

但是它们通常用于HTML，偶尔也有一些HTML的特定功能，比如escaping（换码），
这使得它能过向HTML中插入值而不担心其中是否有HTML中的特殊字符。

"""


# 支持的语法
"""
上下文中的数据使用双大括号插入：
<p>Welcome, {{user_name}}!</p>

圆点将访问对象的属性或者字典的值，并且如果结果值是可调用的，它将被自动调用。


你还可以使用被称作过滤器的函数来修改值。过滤器通过一个竖线（管道符）来调用：
<p>Short name: {{story.subject|slugify|lower}}</p>

建立一个有趣的网站通常需要至少一点决策，条件语句要是可用的：
{% if user.is_logged_in %}
    <p>Welcome, {{ user.name }}!</p>
{% endif %}

循环让我们在页面中包含数据集合：
<p>Products:</p>
<ul>
{% for product in product_list %}
    <li>{{ product.name }}: {{ product.price|format_price }}</li>
{% endfor %}
</ul>

正如其他编程语言，条件和循环语句可以嵌套来构复杂的逻辑结构。
最后，让我们可以为模板添加文档，注释出现在大括号和井号之间：
{# This is the best template ever! #}

作者：treelake
链接：https://www.jianshu.com/p/b5d4aa45e771
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
"""

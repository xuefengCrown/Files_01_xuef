
# 解析阶段将一个模板转换为一个Python函数。再次使用我们的小模板：
"""
<p>Welcome, {{user_name}}!</p>
<p>Products:</p>
<ul>
{% for product in product_list %}
    <li>{{ product.name }}:
        {{ product.price|format_price }}</li>
{% endfor %}
</ul>

"""
##我们的引擎将编译这个模板为python代码。python代码的结果看上去不同寻常，
##因为我们选择了一些快捷方式来产生轻量级和更快的代码。
##下面的python代码为了可读性重新轻微的格式化了：
def render_function(context, do_dots):
    c_user_name = context['user_name']
    c_product_list = context['product_list']
    c_format_price = context['format_price']

    result = []
    #微优化具有启发性，因为它们使用了python的某些奇异的方面，
    #但是别在你自己的代码中过度使用它。
    append_result = result.append # 加速,因为避免了再花时间去查找对象的append属性
    extend_result = result.extend # [1,2].extend([4,5])
    #查找一个本地变量名的速度要比查找一个全局或内置的名称快。
    #我们习惯于str是一个总是可获得的内置函数，但是python仍然不得不在每次使用它时查找变量名。
    #将它放在一个本地变量中又为我们节省了一小块的时间，因为本地的要比内建的快。
    to_str = str

    extend_result([
        '<p>Welcome, ',
        to_str(c_user_name),
        '!</p>\n<p>Products:</p>\n<ul>\n'
    ])
    for c_product in c_product_list:
        extend_result([
            '\n    <li>',
            to_str(do_dots(c_product, 'name')),
            ':\n        ',
            to_str(c_format_price(do_dots(c_product, 'price'))),
            '</li>\n'
        ])
    append_result('\n</ul>\n')
    return ''.join(result)
"""
每个模板都被转换为一个render_function函数，其接受一个叫做context的数据字典。
函数体先解包上下文字典中的数据到本地变量，因为对于数据的重复使用这样会快些。
所有的上下文数据以加上c_前缀的形式变为本地变量这样我们可以自由使用本地变量名
而不用担心命名冲突。

模板的结果将是一个字符串。从部件构建一个字符串最快的方式就是创建一个字符串列表，
然后将它们组合在一起。result就是一个字符串列表。因为我们将添加字符串到这个列表中，
我们捕捉了它的append和extend方法赋给本地变量result_append和result_extend。
最后一个创建的本地变量是一个内置方法str的速记--to_str。

这些形式的快捷键并不寻常。让我们看得更仔细些：在python中，一个被对象调用的方法
如result.append("hello")分两步执行。首先，append属性从result对象中获取，然后取得的值
被作为函数调用，传递参数“hello”给它。尽管我们习惯于看到这些步骤被一起执行，实际上它们是分开的。
如果你储存了第一步的结果，那么你将在储存的结果上执行第二步。


在{{...}}中的表达式将被计算，转换为字符串，并被添加到result。
表达式中的点将被传入渲染函数的do_dots函数处理，因为加点的表达式的意义取决于
context中的数据形式：它可能是属性访问、子项目获取或者是一个调用。
"""

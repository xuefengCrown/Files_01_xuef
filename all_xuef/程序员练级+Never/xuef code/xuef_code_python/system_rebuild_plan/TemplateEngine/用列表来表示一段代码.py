"""
def render_function(context, do_dots):
    c_user_name = context['user_name']

    result = []
    for c_product in c_product_list:
        pass
    append_result('\n</ul>\n')
    return ''.join(result)
"""
from code_build import CodeBuilder

cblock = CodeBuilder()
cblock.add_line("def render_function(context, do_dots):")
cblock.indent()

#我们创建了一个片段叫vars_code。之后我们将在该片段中写上变量提取的语句。
#vars_code对象使我们保留了一个函数中的位置，它将在我们得到需要的信息后被填补。
vars_code = code.add_section()

cblock.add_line("c_user_name = context['user_name']")
cblock.add_line("result = []")
cblock.add_line("for c_product in c_product_list:")

cblock.indent()
cblock.add_line("pass")
cblock.dedent()
cblock.add_line("append_result('\\n</ul>\\n')")
cblock.add_line("return ''.join(result)")
cblock.dedent()

print(cblock)
r = cblock.get_globals()
print(r)



## 相应的 Python 代码
def render(context, do_dot):
    result = []
    result.extend(["<p>Welcome,",
                  context['user_name'],
                  "\n<p>Products:</p>\n<ul>\n"])
    for product in context['product_list']:
        result.extend(["    <li>",
                      str(do_dot(product, "name")),
                      ":\n",
                      str(context['format_price'](do_dot(product, "price"))),
                      "    </li>\n"])
    result.append("</ul>")
    return result


format_price = lambda x: x
product_list = [{'name': '冰箱', 'price': 3000},
                {'name': '洗衣机', 'price': 2000}]
do_dot = lambda obj, attr: obj[attr]
context = {
    'user_name': 'xuef',
    'format_price': format_price,
    'product_list': product_list
    }

res = render(context, do_dot)
print("".join(res))

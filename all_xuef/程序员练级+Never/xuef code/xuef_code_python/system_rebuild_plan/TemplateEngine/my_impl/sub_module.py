


# 模板表达式-->python表达式
"""
user.name.localized|upper|escape --> escape(upper(user['name']['localized']))
escape(upper(do_dots(user, 'name', 'localized')))
"""
def _expr_code1(expr):
    """Generate a Python expression for `expr`."""
    pass

def _expr_code(expr):
        """Generate a Python expression for `expr`."""
        if "|" in expr:
            pipes = expr.split("|")
            code = _expr_code(pipes[0])
            for func in pipes[1:]:
                code = "%s(%s)" % (func, code)
        elif "." in expr:
            dots = expr.split(".")
            code = _expr_code(dots[0])
            args = ", ".join(repr(d) for d in dots[1:])
            code = "do_dots(%s, %s)" % (code, args)
        else:
            code = "%s" % expr
        return code

expr = "user.name.localized|upper|escape"
py_expr = _expr_code(expr)

print(py_expr)




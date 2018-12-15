
"""
模板引擎的核心是Templite类。（它是一个模板，但是它是精简版的）
这个类具有一个小的接口。你可以利用模板中的文本构建一个Templite对象，
然后你可以使用它的render方法来渲染一个特定的上下文（数据的字典）到模板中。

# Make a Templite object.
templite = Templite('''
    <h1>Hello {{name|upper}}!</h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    ''',
    {'upper': str.upper},
)

# Later, use it to render some data.
text = templite.render({
    'name': "Ned",
    'topics': ['Python', 'Geometry', 'Juggling'],
})

"""

"""
我们将模板中的文本在对象创建时传递给它，这样我们就能只做一次编译步骤，然后多次调用
render函数来重用编译结果。
构造函数也接受一个字典来作为初始的上下文。这些数据被存储在Templite对象里，并且之后当模板
被渲染时可以获取。这个位置适合于一些我们希望能随时获取的函数和常量，比如之前例子中的upper函数。
"""

# CodeBuilder
"""
我们的模板引擎的主要工作是解析模板并产生必要的python代码。为了帮助产生python代码，
我们创建了一个CodeBuiler类，当我们构建python代码时它为我们处理簿记。它增加代码行，
管理缩进，最终给我们编译好的python代码。
"""
# 想一下,我们如何用list来表示一段python代码?
# 一个CodeBuilder对象对一整块python代码负责。
class CodeBuilder(object):
    """Build source code conveniently."""

    def __init__(self, indent=0):
        self.code = [] #该列表将被组合到最终的python代码
        self.indent_level = indent

    def add_line(self, line):
        """Add a line of source to the code.
        Indentation and newline will be added for you, don't provide them.
        """
        self.code.extend([" " * self.indent_level, line, "\n"])

    INDENT_STEP = 4      # PEP8 says so!

    def indent(self):
        """Increase the current indent for following lines."""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """Decrease the current indent for following lines."""
        self.indent_level -= self.INDENT_STEP
    #we also use nested CodeBuilders to make it possible to put code at the beginning of
    #the function even though we don't know what it will be until we are nearly done.
    #This lets us keep a reference to a place in the code, and add text to it later.
    #允许我们在某个节点处埋下一段代码位置，稍后往里填代码。
    def add_section(self): # ???
        #python中一个函数中的代码从作用域上来看并不是一体的???
        """Add a section, a sub-CodeBuilder."""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section
    
    def __str__(self): # 递归的
        return "".join(str(c) for c in self.code)

    def get_globals(self):
        """Execute the code, and return a dict of globals it defines."""
        # A check that the caller really finished all the blocks they started.
        assert self.indent_level == 0
        # Get the Python source as a single string.
        python_source = str(self)
        # Execute the source, defining globals, and return them.
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace

import re

class TempliteSyntaxError(ValueError):
    """Raised when a template has a syntax error."""
    pass

# 编译一个模板为python函数的所有工作在Templite构造器里发生。
# 首先上下文被保存：
class Templite():
    def __init__(self, text, *contexts):
        """Construct a Templite with the given `text`.

        `contexts` are dictionaries of values to use for future renderings.
        These are good for filters and global values.

        """
        self.context = {}
        for cxt in contexts:
            self.context.update(cxt)#我们简单的创建了一个所有上下文字典组合而成的字典

        self.all_vars = set()
        self.loop_vars = set()

        # We construct a function in source form, then compile it and hold onto
        # it, and execute it to render the template.
        code = CodeBuilder()
        #我们的python函数将被称为render_function，
        #它接受两个参数：一个是上下文数据字典，一个是实现点属性访问的do_dots函数。
        code.add_line("def render_function(context, do_dots):")
        code.indent()
        
        #我们创建了一个片段叫vars_code。之后我们将在该片段中写上变量提取的语句。
        #vars_code对象使我们保留了一个函数中的位置，它将在我们得到需要的信息后被填补。
        vars_code = code.add_section()
        code.add_line("result = []")
        code.add_line("append_result = result.append")
        code.add_line("extend_result = result.extend")
        code.add_line("to_str = str")

        buffered = []
        #定义一个内部函数来帮助我们缓冲输出字符串
        def flush_output():
            """Force `buffered` to the code builder."""
            if len(buffered) == 1:
                code.add_line("append_result(%s)" % buffered[0])
            elif len(buffered) > 1:
                code.add_line("extend_result([%s])" % ", ".join(buffered))
            del buffered[:]

        #当我们解析控制流结构时，我们希望检查它们是否是合理地嵌套了。
        #ops_stack列表是一个字符串堆栈
        ops_stack = []

        #re.split函数将使用正则分割一个字符串。
        #我们的模式在括号里，匹配的符号将被用来分割字符串，分割出的字符串将组成列表返回。
        # Split the text to form a list of tokens.
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)

        #根据类型来分割它们，我们就可以分别处理每个类型。
        #编译代码是一个关于这些标记的循环
        for token in tokens:
            if token.startswith('{#'):
                # Comment: ignore it and move on.
                continue
            elif token.startswith('{{'):
                # An expression to evaluate.
                expr = self._expr_code(token[2:-2].strip())
                buffered.append("to_str(%s)" % expr)
                
            #第三种情况是{% ... %}标签。要将它们变为python的控制结构。
            elif token.startswith('{%'):
                # Action tag: split into words and parse further.
                flush_output()
                words = token[2:-2].strip().split()
                """
                {% if user.is_logged_in %}
                    <p>Welcome, {{ user.name }}!</p>
                {% endif %}
                """
                if words[0] == 'if':
                    # An if statement: evaluate the expression to determine if.
                    if len(words) != 2: # if标签只能有一个表达式
                        self._syntax_error("Don't understand if", token)
                    ops_stack.append('if')
                    code.add_line("if %s:" % self._expr_code(words[1]))
                    code.indent()
                elif words[0] == 'for':
                    # A loop: iterate over expression result.
                    if len(words) != 4 or words[2] != 'in':
                        self._syntax_error("Don't understand for", token)
                    ops_stack.append('for')
                    self._variable(words[1], self.loop_vars)
                    code.add_line(
                        "for c_%s in %s:" % ( #所有的模板变量都加上c_前缀被转换为python变量
                            words[1],
                            self._expr_code(words[3])
                        )
                    )
                    code.indent()
                elif words[0].startswith('end'):
                    # Endsomething.  Pop the ops stack.
                    #注意这里真正需要的工作只是最后一行：取消函数源码的缩进。
                    #余下的语句都是错误检查来保证模板被正确地组织了。这在程序翻译代码中很常见。                    
                    if len(words) != 1:
                        self._syntax_error("Don't understand end", token)
                    end_what = words[0][3:]
                    if not ops_stack:
                        self._syntax_error("Too many ends", token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error("Mismatched end tag", end_what)
                    code.dedent() #在之前的if或for语句末尾加上取消缩进
                else:
                    self._syntax_error("Don't understand tag", words[0])
            else:
                # Literal content.  If it isn't empty, output it.
                if token:
                    #The repr function supplies the quotes around the string for us,
                    #and also provides backslashes where needed
                    buffered.append(repr(token))

        if ops_stack:
            self._syntax_error("Unmatched action tag", ops_stack[-1])

        flush_output()

        for var_name in self.all_vars - self.loop_vars:
            vars_code.add_line("c_%s = context[%r]" % (var_name, var_name))

        code.add_line("return ''.join(result)")
        code.dedent()
        self._render_function = code.get_globals()['render_function']

    # 模板expr-->python expr的转换
    #As with expressions in any language, ours are built recursively: big expressions a
    #re composed of smaller expressions.
    def _expr_code(self, expr):
        """Generate a Python expression for `expr`."""
        if "|" in expr:
            pipes = expr.split("|")
            code = self._expr_code(pipes[0])
            for func in pipes[1:]:
                self._variable(func, self.all_vars)
                code = "c_%s(%s)" % (func, code)
        elif "." in expr:
            dots = expr.split(".")
            code = self._expr_code(dots[0])
            args = ", ".join(repr(d) for d in dots[1:])
            code = "do_dots(%s, %s)" % (code, args)
        else:
            self._variable(expr, self.all_vars)
            code = "c_%s" % expr
        return code

    def _syntax_error(self, msg, thing):
        """Raise a syntax error using `msg`, and showing `thing`."""
        raise TempliteSyntaxError("%s: %r" % (msg, thing))

    def _variable(self, name, vars_set):
        """Track that `name` is used as a variable.
        Adds the name to `vars_set`, a set of variable names.
        Raises an syntax error if `name` is not a valid name.
        """
        if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
            self._syntax_error("Not a valid name", name)
        vars_set.add(name)

    def render(self, context=None):
        """Render this template by applying it to `context`.
        `context` is a dictionary of values to use in this rendering.
        """
        # Make the complete context we'll use.
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context, self._do_dots)

    def _do_dots(self, value, *dots):
        """Evaluate dotted expressions at runtime."""
        for dot in dots:
            try:
                value = getattr(value, dot)
            except AttributeError:
                value = value[dot]
            if callable(value):
                value = value()
        return value








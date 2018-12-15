# 几本书，关于程序的本质
"""
<How to Design Programs>: https://htdp.org/2018-01-06/
<Composing Programs>
<SICP>
"""

# 列表的本质
# 我们思维不够活跃，我们想象力不够
# 想一下,我们如何用list来表示一段python代码?
# CodeBuilder很简单：它不知道函数的定义，只拥有代码行。
# 这保持CodeBuilder在实现和使用上的简便性。
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
    def add_section(self):
        """Add a section, a sub-CodeBuilder."""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

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
    
    def __str__(self):
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


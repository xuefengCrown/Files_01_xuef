
#add variables to our interpreter.
"""
我们需要一个保存变量值的指令，STORE_NAME;
一个取变量值的指令LOAD_NAME;
和一个变量到值的映射关系。

目前，我们会忽略命名空间和作用域，所以我们可以把变量和值的映射直接存储在解释器对象中。
最后，我们要保证what_to_execute除了一个常量列表，还要有个变量名字的列表。
"""


# a friendly compiler transforms `s` into:
"""
def s():
    a = 1
    b = 2
    print(a + b)
"""
what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),
                     ("STORE_NAME", 0),
                     ("LOAD_VALUE", 1),
                     ("STORE_NAME", 1),
                     ("LOAD_NAME", 0),
                     ("LOAD_NAME", 1),
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [1, 2],
    "names":   ["a", "b"] }


class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def LOAD_VALUE(self, number):
        self.stack.append(number)
 
    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)
 
    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val
 
    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)
 
    def parse_argument(self, instruction, argument, what_to_execute):
        """ Understand what the argument to each instruction means."""
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]
 
        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        elif instruction in names:
            argument = what_to_execute["names"][argument]
 
        return argument
 
    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)
 
            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)
            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(argument)

    #可用Python的getattr函数在运行时动态查找方法
    def better_run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)


interp = Interpreter()
interp.better_run_code(what_to_execute)




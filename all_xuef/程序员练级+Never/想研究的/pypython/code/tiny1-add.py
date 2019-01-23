
##instruction set:
what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5] }


#Python解释器是一个栈机器，所以它必须通过操作栈来完成这个加法。
"""
LOAD_VALUE这条指令告诉解释器把一个数压入栈中，但指令本身并没有指明这个数是多少。
指令需要一个额外的信息告诉解释器去哪里找到这个数。所以我们的指令集有两个部分：
指令本身和一个常量列表。
"""

#为什么不把数字直接嵌入指令之中？
"""
想象一下，如果我们加的不是数字，而是字符串。我们可不想把字符串这样的东西加到指令中，
因为它可以有任意的长度。另外，我们这种设计也意味着我们只需要对象的一份拷贝，比如这个加法 7 + 7,
现在常量表 "numbers"只需包含一个7。
"""

#
"""
你可能会想为什么会需要除了ADD_TWO_VALUES之外的指令。的确，对于我们两个数加法，这个例子是有点
人为制作的意思。然而，这个指令却是建造更复杂程序的轮子。比如，就我们目前定义的三个指令，
只要给出正确的指令组合，我们可以做三个数的加法，或者任意个数的加法。

同时，栈提供了一个清晰的方法去跟踪解释器的状态，这为我们增长的复杂性提供了支持。
"""

#解释器对象需要一个栈，它可以用一个列表来表示。
##它还需要一个方法来描述怎样执行每条指令。
class Interpreter:
    def __init__(self):
        self.stack = []
 
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

    #解释器还需要一样东西：一个能把所有东西结合在一起并执行的方法。
    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        numbers = what_to_execute["numbers"]
        for each_step in instructions:
            instruction, argument = each_step
            if instruction == "LOAD_VALUE":
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()


interpreter = Interpreter()
interpreter.run_code(what_to_execute)

#有几点要注意。
"""
首先，一些指令需要参数。在真正的Python bytecode中，大概有一半的指令有参数。
像我们的例子一样，参数和指令打包在一起。注意指令的参数和传递给对应方法的参数是不同的。

第二，指令ADD_TWO_VALUES不需要任何参数，它从解释器栈中弹出所需的值。
这正是以栈为基础的解释器的特点。
"""



















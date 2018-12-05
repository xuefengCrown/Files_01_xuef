"""
你可能会想为什么会需要除了ADD_TWO_VALUES之外的指令。
的确，对于我们两个数加法，这个例子是有点人为制作的意思。
然而，这个指令却是建造更复杂程序的轮子。
比如，就我们目前定义的三个指令，只要给出正确的指令组合，我们可以做三个数的加法，
或者任意个数的加法。同时，栈提供了一个清晰的方法去跟踪解释器的状态，
这为我们增长的复杂性提供了支持。
"""
what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "numbers": [7, 5] }

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







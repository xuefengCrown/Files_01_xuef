
"""
菜单驱动的文本编辑器的 UML 类图，使用“命令”设计模式
实现。各个命令可以有不同的接收者（实现操作的对象）。对
PasteCommand 来说，接收者是 Document。对 OpenCommand 来说，
接收者是应用程序。

“命令”模式的目的是解耦调用操作的对象（调用者）和提供实现的对象
（接收者）。

这个模式的做法是，在二者之间放一个 Command 对象，让它实现只有
一个方法（execute）的接口，调用接收者中的方法执行所需的操作。
这样，调用者无需了解接收者的接口，而且不同的接收者可以适应不同
的 Command 子类。调用者有一个具体的命令，通过调用 execute 方法
执行。

Gamma 等人说过：“命令模式是回调机制的面向对象替代品。”问题是，
我们需要回调机制的面向对象替代品吗？有时确实需要，但并非始终需
要。
"""

class MacroCommand:
    """一个执行一组命令的命令"""
    def __init__(self, commands):
        self.commands = list(commands) # 

    # 调用 MacroCommand 实例时，self.commands 中的各个命令依序执行。
    def __call__(self):
        for command in self.commands: # 
            command()



#很多情况下，在 Python 中使用函数或可调用对象实现回调更自然








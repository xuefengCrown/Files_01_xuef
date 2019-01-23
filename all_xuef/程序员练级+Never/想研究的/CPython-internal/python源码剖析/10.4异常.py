
sc = """
1 / 0
"""

import dis

dis.dis(sc)
"""

  2           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (0)
              4 BINARY_TRUE_DIVIDE
              6 RETURN_VALUE

"""
##
"""
case BINARY_DIVIDE:
    if (!_Py_QnewFlag) {
        w = POP();
        v = TOP();
        x = PyNumber_Divide(v, w);
        Py_DECREF(v);
        Py_DECREF(w);
        SET_TOP(x);
        if (x != NULL) continue;
        break;
    }
"""
###异常在哪里抛出？被抛到了何处？


##展开栈帧
"""
PyFrameObject 对象是 Python虚拟机对栈帧的模拟，当发生函数调用时，虚拟机会创建一个与
被调用函数对应的 PyFrameObject对象(栈帧)，并通过该对象的 f_back 连接到调用者对应的
PyFrameObject 对象。这样就形成了一条 PyFrameObject对象链表。
"""
def h():
    1/0
def g():
    h()
def f():
    g()

f()

##
"""
在 Python虚拟机处理异常的流程中，涉及了一个 traceback 对象，在这个对象中记录栈帧链表的信息，
Python虚拟机利用这个对象来将栈帧链表中每个栈帧的当前状态可视化。

Python虚拟机意识到有异常抛出，并创建了 traceback对象后，它会在当前栈帧中寻找 except语句，
以寻找开发者指定的捕捉异常的动作，如果没找到，那么Python 虚拟机将退出当前的活动栈帧，并沿着
栈帧链表向上回退到上一个栈帧。
在上栗中，即从函数 h对应的 PyFrameObject对象沿着 f_back回退到 函数g 对应的 PyFrameObject对象。

PyEval_EvalFrameEx 返回到什么地方了？大难可能让你迷惑，返回到 PyEval_EvalFrameEx里去了。
PyEval_EvalFrameEx是 Python 虚拟机的主要实现代码。当 Python虚拟机运行时，这个函数是会被
递归调用的。
从它的函数名上也可以看出来，这是一个与某个 PyFrameObject对象的执行有关的函数，既然
PyFrameObject对象有一个链表，那么 PyEval_EvalFrameEx也就只能通过递归与链表结构对应了。

举个例子，当 Python虚拟机执行函数 g时，它是在 PyEval_EvalFrameEx中执行与g 对应的 PyFrameObject
对象中的字节码指令序列。当在 g中调用h 时， Python虚拟机为 h 创建新的 PyFrameObject 对象，同时
递归调用 PyEval_EvalFrameEx，不过这回是在其中执行与 h 对应的 PyFrameObject 对象中的字节码指令
序列了。所以当在 h中发生异常，导致 PyEval_EvalFrameEx 结束时，自然要返回到与函数 g 对应的
PyEval_EvalFrameEx中。 由于在返回时，设置的 retval 为NULL，所以 Python虚拟机在回到与 g 对应的
PyEval_EvalFrameEx 中后再次意识到有异常产生。接下来的动作就顺理成章了。同样是创建 traceback对象，
同样是寻找程序员指定的 except，如果没有指定异常捕捉动作，那么同样也要退出与 g对应的 PyEval_EvalFrameEx，
而返回到与 f 对应的 PyEval_EvalFrameEx。
"""
###这个沿着栈帧不断回退的过程我们称之为栈帧展开。
###在此过程中，Python虚拟机不断创建与各个栈帧对应的 traceback对象，并将其链接成链表。

"""
变量 why指示 Python虚拟机当前是否发生了异常。
而 PyTryBlock 对象则指示 Python 虚拟机 程序员是否为异常设置了 except代码块和
finally代码块。
"""















































































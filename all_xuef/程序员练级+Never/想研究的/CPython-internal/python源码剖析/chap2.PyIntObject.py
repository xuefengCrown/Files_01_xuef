

#如何高效实现，是关键。

##整数对象池


##PyIntObject def
"""
[intobject.h]

typedef struct {
    Py_ssize_t ob_recnt;
    struct _typeobject *ob_type;
    long ob_ival;
} PyIntObject;

typedef struct _object {
    Py_ssize_t ob_recnt;
    struct _typeobject *ob_type;
} PyObject;
"""
###可见，PyIntObject对象只是对C 的原生类型 long 的一个简单包装。
###与对象相关的元信息实际上都是保存在与对象对应的类型对象中的，对于 PyIntObject，该
###类型对象是 PyInt_Type



##对象的创建与维护
###对象创建的 3 种途径
"""
1. 可以通过 Python暴露的 C API
2. 通过类型对象完成创建动作。int(2)
"""

##在运行期间，一个个整数对象在内存中并不是独立存在的，而是形成了一个整数对象系统???
###2.2.2 小整数对象
"""
它们使用最频繁?!小整数的界限是不明确的，你可以自己指定，通过修改源代码。

PyIntObject 对象是不可变对象，那么对象池里的每个 PyIntObject都能够被任意共享。

"""






















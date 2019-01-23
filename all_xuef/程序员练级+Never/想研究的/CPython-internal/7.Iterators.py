
#关键问题
"""
为什么需要 Iterators?
1. 更方便的接口
2. 我们不需要序列的长度
3. 我们可以 iterate everything (tree...)
"""

##序列对象是静态的,但是 seqiterobject 是动态的
##我们需要维护一个额外的索引
"""
typedef struct {
    PyObject_HEAD
    long it_index;
    PyObject *it_seq;
} seqiterobject;
"""
###类比于 scope,随着语句的执行，作用域中的bindings 是可能改变的。


##自定义迭代器

#a calculator

def str2ast(exp):
    """
    (1+2*3)*(4+5)-->
    ['*', ['+', 1, ['*', 2, 3]], ['+', 4, 5]]
    """
    pass

def eval_ast(ast):
    """
    ast: ['*', ['+', 1, ['*', 2, 3]], ['+', 4, 5]]
    """
    # your code
    pass


def test_eval_ast(ast):
    eval_ast(ast)


if __name__ == '__main__':
    ast = ['*', ['+', 1, ['*', 2, 3]], ['+', 4, 5]]
    test_eval_ast(ast)



















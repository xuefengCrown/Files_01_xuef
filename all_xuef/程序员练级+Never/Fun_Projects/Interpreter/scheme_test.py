from scheme import r2

def test_scheme():
    #Number
    c0 = "1"
    #变量
    c1 = "x"
    #函数 (我们的函数只接受一个参数)
    c2 = "((lambda (x) (* 2 x)) 8)"
    #绑定
    c3 = """(let ((x 2))
                   (let ((f (lambda (y) (* x y))))
                        (f 3)))"""
    
    c32 = "(let ((x 4) (y (* 3 3))) (* x y))" #scheme使用()来区分逻辑块
    #过程调用
    
    #算术表达式 (ope e1 e2)
    c5 = "(+ 2 (* 7 6))"
    c52 = "(+ (* 8 9) (* 8 1))"
    c61 = "(- 2 1)"
    c62 = "(/ 2 1)"
    assert(r2(c0) == 1)
    assert(r2(c2) == 16)
    assert(r2(c3) == 6)
    assert(r2(c32) == 36)
    assert(r2(c5) == 44)
    assert(r2(c52) == 80)
    assert(r2(c61) == 1)
    assert(r2(c62) == 2)
    
#print(analyze(tokenize(c22)))
if __name__ == '__main__':
    test_scheme()

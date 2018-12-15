
##yield from
## RESULT = yield from EXPR
## yield from 会在子生成器迭代完成之后(也就是抛了StopIteration as e后),
## 取出e中的return val交给 RESULT

#pep380
#RESULT = yield from EXPR 可以简化为

"""
_i: 子生成器，同时也是一个迭代器
_y: 子生成器生产的值
_r: yield from表达式最终的值
_s: 调用方通过send()发送的值
_e: 异常对象
"""
_i = iter(EXPR) # EXPR是一个可迭代对象， _i其实是子生成器

try:
    _y = next(_i) # 预激子生成器，把产出的第一个值存在 _y中
except StopIteration as _e:
    _r = _e.value
else:
    while 1: # 尝试执行这个循环，委托生成器会阻塞
        _s = yield _y # yield 子生成器的值，等待调用方send值进来，并用 _s接收
        try:
            _y = _i.sned(_s) # 转发 _s, 并且尝试向下执行
        except StopIteration as _e:
            _r = _e.value
            break
RESULT = _r


# 总结
"""
1. 子生成器生产的值，都是直接传给调用方的。调用方send的值都是直接传给子生成器的
2. 子生成器退出时，最后的return EXPR，会触发一个StopIteration(EXPR)异常
3. yield from表达式的值，是子生成器终止时，传递给 StopIteration异常的第一个参数
4. 如果调用时出现 StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上冒泡
5. 传入委托生成器的异常里，除了 GeneratorExit外，其他的都会传递给子生成器的throw方法
6. 如果在委托生成器上调用close或传入 GeneratorExit异常，会调用子生成器的 close
"""


























            


























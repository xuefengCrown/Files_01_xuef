
# (3,4) 表示什么?

# 可以是 rational number
# 可以是 复数
# ...


## 我们需要给它添加 标记 (tagged data)

#Our goal is to write a universal addition procedure.

"""
(define (add-numbers num1 num2)
  (cond ((and (equal? (type-tag num1) 'rational)
              (equal? (type-tag num2) 'rational))
         (add-rational num1 num2))
        ((and (equal? (type-tag num1) 'complex)
              (equal? (type-tag num2) 'complex))
         (add-complex num1 num2))
        ((and (equal? (type-tag num1) 'rational)
              (equal? (type-tag num2) 'complex))
         (add-rational-complex num1 num2))
        (else
         (add-rational-complex num2 num1))))
"""
## Weaknesses of Tagged Data
"""
1. 我们必须手动为每种类型添加标记然后包含近进我们的通用方法中
2. 我们必须保证没有两个过程重名!
"""



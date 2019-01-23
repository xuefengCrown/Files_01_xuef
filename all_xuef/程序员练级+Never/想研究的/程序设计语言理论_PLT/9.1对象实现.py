
#An object is just a value that dispatches on a given name.
##对象是对给定名称进行分派的一种值。


#10.1.4 构造器
##构造器就是在对象构造时调用的函数。
"""
(define (o-constr-1 x)
  (lambda (m)
    (case m
      [(addX) (lambda (y) (+ x y))])))

(test (msg (o-constr-1 5) 'addX 3) 8)
(test (msg (o-constr-1 2) 'addX 3) 5)
"""
##构造器的两次调用不会相互干扰。

#10.1.5 状态
"""
(define (o-state-1 count)
  (lambda (m)
    (case m
      [(inc) (lambda () (set! count (+ count 1)))]
      [(dec) (lambda () (set! count (- count 1)))]
      [(get) (lambda () count)])))

(test (let ([o1 (o-state-1 3)]
            [o2 (o-state-1 3)])
        (begin (msg o1 'inc)
               (msg o1 'inc)
               (+ (msg o1 'get)
                  (msg o2 'get))))
      (+ 5 3))
"""
#请注意，对一个对象进行赋值不会影响到另一个对象



#10.1.7 静态成员
##that are common to all instances of the “same” type of object.
"""
(define o-static-1
  (let ([counter 0])
    (lambda (amount)
      (begin
        (set! counter (+ 1 counter))
        (lambda (m)
          (case m
            [(inc) (lambda (n) (set! amount (+ amount n)))]
            [(dec) (lambda (n) (set! amount (- amount n)))]
            [(get) (lambda () amount)]
            [(count) (lambda () counter)]))))))
"""
##测试就是构造多个对象，并确保它们每一个都影响了全局的 count
"""
(test (let ([o (o-static-1 1000)])
        (msg o 'count))
      1)
 
(test (let ([o (o-static-1 0)])
        (msg o 'count))
      2)
"""

#10.1.8 Objects with Self-Reference
#目前为止，我们的对象还只是打包的实名函数；或者你可以这么说，有多个实名入口点的函数。
#our objects have simply been packages of named functions:
#functions with multiple named entry-points, if you will.

#可以看到，很多对象系统中被认为很重要的特性可以通过函数和作用域实现，事实上
#很长一段时间里懂得 lambda  的程序员的确是这么做的，只是没有给这种做法起名字罢了。

#10.1.8.1 Self-Reference Using Mutation
"""
One characteristic that actually distinguishes object systems is that each object
is automatically equipped with a reference to the same object, often called self or this.

(define o-self!
  (let ([self 'dummy])
    (begin
      (set! self
            (lambda (m)
              (case m
                [(first) (lambda (x) (msg self 'second (+ x 1)))]
                [(second) (lambda (x) (+ x 1))])))
      self)))
"""

#10.1.8.2 Self-Reference Without Mutation
"""
(define o-self-no!
  (lambda (m)
    (case m
      [(first) (lambda (self x) (msg/self self 'second (+ x 1)))]
      [(second) (lambda (self x) (+ x 1))])))

(define (msg/self o m . a)
  (apply (o m) o a))
"""
#python


#10.1.9 Dynamic Dispatch
"""
(define (mt)
  (let ([self 'dummy])
    (begin
      (set! self
            (lambda (m)
              (case m
                [(add) (lambda () 0)])))
      self)))
 
(define (node v l r)
  (let ([self 'dummy])
    (begin
      (set! self
            (lambda (m)
              (case m
                [(add) (lambda () (+ v
                                     (msg l 'add)
                                     (msg r 'add)))])))
      self)))


With these, we can make a concrete tree:
(define a-tree
  (node 10
        (node 5 (mt) (mt))
        (node 15 (node 6 (mt) (mt)) (mt))))

And finally, test it:
(test (msg a-tree 'add) (+ 10 5 15 6))

"""
##注意到，在测试案例中，还有在 node  的 add  方法中，都调用了 add  方法而没有检查接收方
##是 mt  还是 node  。运行时系统提取出接收方的 add  方法并执行。用户的程序中没有条件表达
##式，这正是动态分发的精髓。



#10.2 Member Access Design Space
##The lower-right quadrant corresponds closely with languages that use hash-tables
##to represent objects. Then the name is simply the index into the hash-table.



#10.3 What (Goes In) Else?
"""
another reason for an else clause, which is to “chain” control to another, parent, object.
This is called inheritance.
"""
##One answer could be that it is simply another object.
"""
(case m
  ...
  [else (parent-object m)])
"""


#10.3.1 Classes
"""
(define (node/size parent-maker v l r)
  (let ([parent-object (parent-maker v l r)]
        [self 'dummy])
    (begin
      (set! self
            (lambda (m)
              (case m
                [(size) (lambda () (+ 1
                                     (msg l 'size)
                                     (msg r 'size)))]
                [else (parent-object m)])))
      self)))
 
(define (mt/size parent-maker)
  (let ([parent-object (parent-maker)]
        [self 'dummy])
    (begin
      (set! self
            (lambda (m)
              (case m
                [(size) (lambda () 0)]
                [else (parent-object m)])))
      self)))

(define a-tree/size
  (node/size node
             10
             (node/size node 5 (mt/size mt) (mt/size mt))
             (node/size node 15
                        (node/size node 6 (mt/size mt) (mt/size mt))
                        (mt/size mt))))

(test (msg a-tree/size 'add) (+ 10 5 15 6))
(test (msg a-tree/size 'size) 4)
"""
##class NodeSize extends Node { ... }


##当程序员调用Java的类构造器时，它实际上构造了继承链上的所有对象（当然，编译器可能
##会对此优化，只需要进行一次构造器调用和一次对象分配）。































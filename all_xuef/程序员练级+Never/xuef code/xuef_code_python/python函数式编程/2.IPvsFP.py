
"""
A language is imperative because each statement is a command,
which changes the state in some way.
"""
#python 各种语句及其本质
"""
Our general focus is on the assignment statement and how it changes state.
Python has other statements, such as  global or  nonlocal , which modify the rules for
variables in a particular namespace. Statements like  def ,  class , and  import change
the processing context. Other statements like  try ,  except ,  if ,  elif , and  else act
as guards to modify how a collection of statements will change the computation's
state. Statements like  for and  while , similarly, wrap a block of statements so that the
statements can make repeated changes to the state of the computation. The focus of
all these various statement types, however, is on changing the state of the variables.
"""
#我们主要关注赋值语句以及它如何改变状态。
#其他语句
#global or nonlocal，修改变量的搜索空间(search namespace)
#def, class, import 改变 the procession context
#Other statements like try,except,if act as guards to modify how a collection of statements
# will change the computation's state.
#for and  while , similarly, wrap a block of statements so that the
# statements can make repeated changes to the state of the computation. 


#函数式风格的程序更容易理解。声明式风格有着混乱的状态。


#commutative && associative ?可交换的与可结合的???
#求值顺序:应用序与正则序
"""
When functions are commutative or associative, then changes to the order
of evaluation might lead to different objects being created. This might have
performance improvements with no changes to the correctness of the results.
"""
# 1+2+3+4
"""
>>> ((1+2)+3)+4
10
>>> 1+(2+(3+4))
10
"""
##In the first case, we fold in values working from left to right. This is the way Python
##works implicitly. Intermediate objects 3 and 6 are created as part of this evaluation.

#What's important for functional design is the idea that the  + operator (or  add()
#function) can be used in any order to produce the same results.













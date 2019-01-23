
#The Big Idea of object oriented programming is to have data that
#knows how to perform computations on itself.

##One of the main advantages of using generic operators is that new modules
##can be designed and added to pre-existing modules without modifying the
##pre-existing code. Object oriented programming is another technique that
##has this advantage.

#The three main ideas that make object-oriented programming possible are
#message passing, local state and inheritance.


#Objects
"""
When we are coding in OOP, we are dealing with objects or "smart data" that
know how to do operations internally and how to interact with other objects.
"""

#Local States
##Message Passing
"""
The way to get things to happen in OOP is to "ask" them to do something for you.

> (ask Matt-Account 'balance)
1000

> (ask Brian-Account 'balance)
10000

> (ask Matt-Account 'deposit 100)
1100

> (ask Brian-Account 'withdraw 200)
9800

> (ask Matt-Account 'balance)
1100

> (ask Brian-Account 'withdraw 200)
9600
"""
#We use the ask procedure to tell objects to carry out a certain action. 

#In the OOP paradigm, the objects have state.
#That is, they have some knowledge about what has happened to them in the past.

#An instance variable will have different values for different instances.
#实例变量互不干扰













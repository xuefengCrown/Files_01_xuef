
#dynamically typed
"""
Lox is dynamically typed. A single variable can hold a Boolean, number, or string
at different points in time.
"""

##how our value representation can dynamically handle different types.

##C
"""
As far as C is concerned, the universe is an undifferentiated array of bytes.
It’s up to us to decide how many of those bytes to use and what they mean.

This is why Python is described as dynamically typed: you don't know the types of the
arguments to this function until you actually run it.
"""
##In order to choose a value representation,
"""
we need to answer two key questions:

·How do we represent the type of a value?
If you try to, say, multiply a number by true, we need to detect that error
at runtime and report it. In order to do that, we need to be able tell what a
value’s type is.

·How do we store the value itself?
We need to not only be able to tell that three is a number, but that it’s
different from the number four. I know, seems obvious, right? But we’re
operating at a level where it’s good to spell these things out.

how do we solve these efficiently?
"""
###sol
"""
Language hackers over the years have come up with a variety of clever ways to
pack the above information into as few bits as possible.
For now, we’ll start with the simplest, classic solution: a tagged union.
A value contains two parts: a type “tag”, and a payload for the actual value.

typedef struct {  
  ValueType type; 
  union {         
    bool boolean; 
    double number;
  } as; 
} Value;
"""

##Lox Values and C Values
"""
wapper c value-->lox value
"""

##Two New Types
"""
We’ve got a running numeric calculator that now does a number of pointless paranoid
runtime type checks.
We can represent other types internally, but there’s no way for a user’s program to ever
create a value of one of those types.

"""













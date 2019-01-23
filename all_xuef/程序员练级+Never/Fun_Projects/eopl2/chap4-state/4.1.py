
#4.1 Computational Effects
"""
But a computation may have effects as well: it may read, print, or
alter the state of memory or a file system.

What’s the difference between producing a value and producing an effect?
An effect is global: it is seen by the entire computation.
"""
##We will be concerned primarily with a single effect: assignment to a location in memory.

##How does assignment differ from binding?
"""
As we have seen, binding is local, but variable assignment is potentially global.
It is about the sharing of values between otherwise unrelated portions of the computation.

Two procedures can share information if they both know about the same location in memory.
A single procedure can share information with a future invocation of itself by
leaving the information in a known location.
"""

##model memory
##We model memory as a finite map from locations to a set of values called the storable values.
"""
For historical reasons, we call this the store.
The storable values in a language are typically, but not always,
the same as the expressed values of the language. This choice is part of the design of a language.

A data structure that represents a location is called a reference.
A location is a place in memory where a value can be stored, and
a reference is a data structure that refers to that place.

The distinction between locations and references may be seen by analogy:
a location is like a file and a reference is like
a URL. The URL refers to the file, and the file contains some data. Similarly,
a reference denotes a location, and the location contains some data.

References are sometimes called L-values.
"""
















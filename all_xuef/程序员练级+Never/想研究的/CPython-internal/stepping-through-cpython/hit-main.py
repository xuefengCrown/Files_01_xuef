
#main
"""
Modules/python.c
  Copies argv
  sets locale
  calls Py_Main
"""

##Breakpoint 3
"""
(gdb) break _PyObject_New
(gdb) c

PyObject
Everything in python is a PyObject. it's a fundamental structure inside of
the Python interpreter.

dicts, lists, tuples and sets, it's also type objects.
strings, integers, floats.
it's stack frames, it's a lot of internal runtime details.
"""

##Protocols in C
"""
Include/abstract.h   Objects/abstract.c

Object
Buffer  tp_as_buffer
Number  tp_as_number
Mapping tp_as_mapping
Sequence tp_as_sequence

"""
##13.20


























[print("{k}: {v}".format(k=k,v=v)) for k,v in globals().items()]

#??
"""
The statements executed by the top-level invocation of the interpreter,
either read from a script file or interactively, are considered part of a module called __main__,
so they have their own global namespace.
"""

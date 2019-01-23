
"""
Sometimes we might want multiple functions to all close over to the same shared data;
the sharing especially matters if some of the functions mutate it and expect the
others to see the result of those mutations.

The recipient then needs a way to choose between the different functions in the group.
This grouping of functions, and the means to select one from the group, is the essence
of an object.

"""

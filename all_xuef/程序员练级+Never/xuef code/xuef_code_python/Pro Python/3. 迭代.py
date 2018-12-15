
"""
Iteration is an option for any type of sequence, but the real advantage comes in
special types of objects that don’t need to load everything in memory all at once.
"""

# The  range object itself doesn’t contain any of the values in the sequence.
# Instead, it generates them one at a time, on demand, during iteration.

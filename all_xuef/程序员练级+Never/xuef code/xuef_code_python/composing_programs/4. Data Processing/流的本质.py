"""
The usefulness of iterators is derived from the fact that the underlying series of data
for an iterator may not be represented explicitly in memory.

An iterator provides a mechanism for considering each of a series of values in turn,
but all of those elements do not need to be stored simultaneously.

Instead, when the next element is requested from an iterator, that element may be
computed on demand instead of being retrieved from an existing memory source.

Iterators allow for lazy generation of a much broader class of underlying sequential
datasets because they do not need to provide access to arbitrary elements of the
underlying series. Instead, iterators are only required to compute the next element
of the series, in order, each time another element is requested.

"""

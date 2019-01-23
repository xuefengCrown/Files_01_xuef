


#Static analysis
"""
All this semantic insight that is visible to us from analysis needs to be stored somewhere.

1.Often, it gets stored right back as attributes on the syntax tree itself—extra fields
in the nodes that aren’t initialized during parsing but get filled in later.

2.Other times, we may store data in a look-up table off to the side. Typically, the keys to
this table are identifiers—names of variables and declarations. In that case, we call it a
symbol table and the values it associates with each key tell us what that identifier refers to.

3.The most powerful bookkeeping tool is to transform the tree into an entirely new data structure
that more directly expresses the semantics of the code. That’s the next section.

"""

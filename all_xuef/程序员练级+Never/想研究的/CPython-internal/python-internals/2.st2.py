
##https://eli.thegreenplace.net/2010/09/20/python-internals-symbol-tables-part-2
#data structure
"""
A more modern translation would be: "The key to understanding a program is to understand
its data structures. With that in hand, the algorithms usually become obvious."

"""
##QAQ
"""
自己在 ast的基础上生成 symbol table,是个不错的练习！

The output of the first pass is a structurally complete symbol table, consisting of
nested entries that model the blocks in the source code. At this stage the symbol table
contains only partial information about symbols, however. Although it already maps all
symbols defined and used in the code, and even flags special cases such as global symbols
and generators, it still lacks some information, such as the distinction between free symbols
that are defined in enclosing scopes and implicitly global symbols. This is the job of the
second pass [9].

"""

#Symbol table entries
"""
The key data structure to study is the symbol table entry, named PySTEntryObject [2]:

typedef struct _symtable_entry {
    PyObject_HEAD
    PyObject *ste_id;
    PyObject *ste_symbols;
    PyObject *ste_name;
    PyObject *ste_varnames;
    PyObject *ste_children;
    _Py_block_ty ste_type;
    int ste_unoptimized;
    int ste_nested;
    unsigned ste_free : 1;
    unsigned ste_child_free : 1;
    unsigned ste_generator : 1;
    unsigned ste_varargs : 1;
    unsigned ste_varkeywords : 1;
    unsigned ste_returns_value : 1;
    int ste_lineno;
    int ste_opt_lineno;
    int ste_tmpname;
    struct symtable *ste_table;
} PySTEntryObject;
"""

##basic: Code Block
"""
Therefore, if we have the following definition in our Python source:

def outer(aa):
    def inner():
        bb = 1
        return aa + bb + cc
    dd = aa + inner()
    return dd
    
The definition of outer creates a block with its body. So does the definition of inner.
In addition, the top-level module in which outer is defined is also a block.
All these blocks are represented by symbol table entries.

"""
def describe_symtable(st, recursive=True, indent=0):
    def print_d(s, *args):
        prefix = ' ' * indent
        print(prefix + s, *args)

    assert isinstance(st, symtable.SymbolTable)
    print_d('Symtable: type=%s, id=%s, name=%s' % (
                st.get_type(), st.get_id(), st.get_name()))
    print_d('  type:', st.get_type())
    print_d('  nested:', st.is_nested())
    print_d('  has children:', st.has_children())
    print_d('  identifiers:', list(st.get_identifiers()))

    if recursive:
        for child_st in st.get_children():
            describe_symtable(child_st, recursive, indent + 5)

import symtable

code = """
def outer(aa):
    def inner():
        bb = 1
        return aa + bb + cc
    dd = aa + inner()
    return dd
"""

st = symtable.symtable(code, '<str>', 'exec')
describe_symtable(st)


##Constructing the symbol table: algorithm outline
"""
Once we have a clear notion in our head of what information the symbol table
eventually contains, the algorithm for constructing it is quite obvious.

The algorithm is divided into two passes [6]. The first pass creates the basic
structure of entries modeling the blocks in the source code and marks some of
the simple information easily available directly in the AST - for example,
which symbols are defined and referenced in each block.

The second pass walks the symbol table and infers the less obvious information
about symbols: which symbols are free, which are implicitly global, etc.

"""













#Listing 3.3: The node data structure used in the python virtual machine
"""
1         typedef struct _node {
2             short		n_type;
3             char		*n_str;
4             int		n_lineno;
5             int		n_col_offset;
6             int		n_nchildren;
7             struct _node	*n_child;
8         } node;
"""

import ast
from pprint import pprint

code_str = """
1 + 2
"""
node = ast.parse(code_str, mode="exec")
ret = ast.dump(node)

pprint(ret)

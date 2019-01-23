
code_str = """
def hello_world():
    return 'hello world'
"""

code_str = """
1 + 2
"""
import parser
from pprint import pprint 
st = parser.suite(code_str)
pprint(parser.st2list(st))
 

import sys
def add_line_number(f):
    count = 1
    for line in f:
        print('%-60s # %d'%(line[:-1], count))
        count += 1

with open("add_line_number.py", 'rt') as f:
    add_line_number(f)


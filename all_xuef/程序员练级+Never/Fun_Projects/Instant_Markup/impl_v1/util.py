
# 以空行来划分块
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    is_code = False
    for line in lines(file):
        if line.startswith('```'): #capture code block
            is_code = (not is_code)
        if line.strip() or is_code:
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

##with open("test_input.txt", "rt") as f:
##    res = blocks(f)
##
##    print(len(list(res)))

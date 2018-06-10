

def begin(*x):
    return x[-1]

args = ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]

print(begin(args))

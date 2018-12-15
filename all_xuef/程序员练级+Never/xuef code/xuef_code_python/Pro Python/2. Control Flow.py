

def count_lines(filename):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(filename, 'r').readlines())
    except IOError:
        # Something went wrong reading the file.
        return 0
"""
By changing the code to accept  IOError explicitly, the  except block will only execute if there was a
problem accessing the file from the filesystem. Any other errors, such as a  filename that’s not even a
string, will simply raise outside of this function, to be handled by some other piece of code.
"""

# countdown.py
#
# A simple generator function

# The function only executes on next()
def countdown(n):
    print ("Counting down from", n)
    while n > 0:
        yield n # 返回n,生成器悬停于此。
        # yield produces a value, but suspends the function
        # Function resumes on next call to next()
        n -= 1
    print ("Done counting down")

# Example use
if __name__ == '__main__':
    for i in countdown(10):
        print (i)

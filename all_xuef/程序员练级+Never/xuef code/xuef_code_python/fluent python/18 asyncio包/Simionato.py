##
##Here is an example of using multiprocessing (which is included
##in Python 2.6 and easy_installable in older Python versions)
##to print a spin bar while a computation is running:

import sys, time
import multiprocessing

DELAY = 0.1
DISPLAY = [ '|', '/', '-', '\\' ]

def spinner_func(before='', after=''):
    write, flush = sys.stdout.write, sys.stdout.flush
    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY)
        msg = before + DISPLAY[pos] + after
        write(msg); flush()
        write('\x08' * len(msg))
        time.sleep(DELAY)

def long_computation():
    # emulate a long computation
    time.sleep(10)

if __name__ == '__main__':
    spinner = multiprocessing.Process(
        None, spinner_func, args=('Please wait ... ', ''))
    spinner.start()
    try:
        long_computation()
        print 'Computation done'
    finally:
        spinner.terminate()









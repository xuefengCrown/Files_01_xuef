
import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
ender.alive
#True
del s1
ender.alive
#True
s2 = 'spam'
#Gone with the wind...
ender.alive
#False

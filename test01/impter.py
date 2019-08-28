from test01.imptee import foo, show
import sys
def test1():
    a = 1
    print('a', a)
    print('locals:', locals())
    print('globals:', globals())

test1()

print('modules:', sys.modules)
print('locals:', locals())
print('globals:', globals())
show()
foo = ['a']
print('2:', globals())
print('foo from impter:', foo)
print('impter:', id(foo))
show()


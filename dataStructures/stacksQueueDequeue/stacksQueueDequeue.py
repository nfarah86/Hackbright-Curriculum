# from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
	myStack = Stack()
	for ch in mystr:
		myStack.push(ch)
	revstr = ' '
	while not myStack.isEmpty():
		levstr = myStack.pop()
		revstr += levstr
		
	return revstr



print revstring('apple')
print revstring('x')
# testEqual(revstring('apple'), 'elppa')
# testEqual(revstring('x'), 'x')
# testEqual(revstring('123456'), '654321')
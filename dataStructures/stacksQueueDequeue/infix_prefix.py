class Stack():
	def __init__(self):
		self.item = []

	def is_Empty(self):
		return True if(len(self.item) == 0) else False
			
	def stack_top(self):
		return self.item[-1]

	def peek(self):
		return self.item[len(self.item) - 1]

	def push_stack(self, ele):
		self.item.append(ele)

	def pop_stack(self):
		return self.item.pop()

	def i_to_p(self, someString):

		prefixList = []

		operators = {"+": 1, "-" : 1, "/" : 2, "*" : 2, "(" : 0, ")" : 0, " " : -1}
		print operators

		string_input_list = list(someString)
		for i in reversed(someString):
			if i not in operators:
				prefixList.append(i)
				print prefixList
			elif i == ')': #closing brace
				print temp2.is_Empty()
				temp2.push_stack(i)
				print temp2.is_Empty()
			elif i =="(": #opening brace
				print i, "print i ("
				item_pop = temp2.pop_stack()
				print item_pop, "because (, pop all stack"
				while item_pop != ")": #closing brace
					print item_pop, "first"
					prefixList.append(item_pop)
					print prefixList
					print i
					item_pop = temp2.pop_stack()
					print item_pop
					print "while"
			else:
				while(not temp2.is_Empty()) and (operators[temp2.peek()]) >= (operators[i]):
					print i, "second"
					prefixList.append(temp2.pop_stack())
				temp2.push_stack(i)



# if operators[temp2.peek()] > operators[i]
# 	prefixList.append(item_pop)
# 	item_pop = temp2.pop_stack()

temp = Stack()
temp.push_stack('3') 
print temp.peek()
temp.push_stack('+') 
print temp.peek()
print temp.stack_top()
print temp.is_Empty()
print "this is the end of first half"
print " "
temp2 = Stack()
temp2.i_to_p("(A+B)")



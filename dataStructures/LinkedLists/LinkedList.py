class Node:
	""" initialize Node class """
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data =  newdata

	def setNext(self, newnext):
		self.next= newnext

class UnorderedList:
	def __init__(self):
		""" creates the unordered list """
		self.head = None
		self.tail = None
		self.length = 0

	def __len__(self):
		""" returns length of list, O(1) """
		return self.length

	def isEmpty(self):
		""" Should return True or False """
		return self.head == None

	def add(self, data):
		""" Adds data to the left most (beginning) of the linked list """
		temp = Node(data) #create an instance 
		if self.head == None: # if list.isEmpty, direct association for head and tail
			self.head = temp 
			self.tail = temp
		else:
			temp.setNext(self.head) # if list had at least 1 item, lets have temp POINT to where self.head is (SET the ref.point)
			self.head = temp   #after we set the ref point, assign temp as the head
		self.length += 1  #notice we didn't do anything with tail.. tail is always going to be the very first item added to the list.
	def append(self, data):
		""" adds data to the right most (end) of the linked list O(n) """
		
		temp = Node(data)  #instantiate the new node
		current = self.head  #create a variable that = self.head; self.head is the beginning of the list
		while current.next != None:  #while current.next (pointer to the next node) is NOT Grounded (== None), iterate through.  once current.next == None, while loop becomes False
			current = current.getNext()  #move the pointer (transversal)
		current.setNext(temp)  #exit the while loop and set self.head's pointer to point to temp:  current --> temp
		self.length += 1

	def appendWithTail(self, data):
		""" appends to the end of the linked list at O(1) """
		temp = Node(data)
		if self.head == None:
			self.head = temp
			self.tail = temp
		else:
			self.tail.next = temp  #need to initialize tail to None in order to do it this way
			self.tail = temp  #assign tail to temp
		self.length += 1

	def pop(self, index = 0):
		""" remove a node at a given index """

		#if statements correct if user didn't type in things right
		if len(self) == 0:
			print "pop from an empty list"
		if type(index) != int:
			print "index must be an integer"
		if index >= self.length or index < 0:
			print "index is not in range of the list's length"
		
		previous = self.head
		current = self.head
		for i in range(index):  #ie range 5 = 0,1,2,3,4  (32,1,3,2,6)
			previous = current  #previous = node current
			current = current.getNext()
		previous.setNext(current.getNext()) #set prevous ref. point to node6
		self.length -= 1
		return current.data

	def popEndOnly(self):
		current = self.head
		previous = self.head

		while current.getNext() != None:
			previous = current
			current = current.getNext()

		self.tail = previous
		self.tail.next = None

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
			    found = True
			else:
			    previous = current
			    current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def insert(self, index, data):
		""" inserts an item at a specific index in a linked list, returns nothing """
		temp = Node(data)
		previous = self.head
		current = self.head
		for i in range(index):
			previous = current
			current = current.getNext()
		previous.next = temp
		previous = temp
		previous.next = current

		##make a case if if index = 0 ## to do

	def index(self, item):
		""" checks to see if the item is in the linked list, if so returns index O(n)"""
		current = self.head
		count = 0
				## trial for 19
		if item == current.data:   # does 19 = 25 NO
			return count 

		while current != None: #does 19 != None : True
			count += 1  #count = 1
			if item == current.data: # does 19 = 19 True; count = 1; exit loop
				return count

			current = current.next

		return "dne"
	def lengthList(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current.getNext()
		return count


	def printSelf(self):
		if self.head != None:
			current = self.head
			while current.getNext() != None:
				print str(current.data)
				current = current.getNext()
			print current

class OrderedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def addOrderedList(self, data):
		""" Add an item in the proper position in the ordered list"""
		current = self.head
		previous = None
		found = False

		# if self.head == None:
		# 	self.head = temp
		# 	self.tail = temp
			
		# 	current = self.head
		# 	previous = self.head
		# current = temp
		
		while not found and current != None:
			# print "DEBUG", current, previous
			if current.data > data:
				found = True
			# else current.next == None and temp > current.data:
			# 	current.setNext(temp)
			# 	temp.setNext(None)
			# 	found = True
			else:
				previous = current
				current = current.next
		
		temp = Node(data)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)
		self.length += 1

	def search(self, data):
		""" Search for an item that maxmizes the use of ordered list O(n) """

		current = self.head
		previous = self.head
		found = False

		while not found:
			if current.data == data:
				found = True
			elif current.data > data:
				return False
			else:
				previous = current
				current.getNext()
		return found

	def printSelf(self):
		if self.head != None:
			current = self.head
			while current.getNext() != None:
				print str(current.data)
				current = current.getNext()
			print current








temp = UnorderedList()
temp.add(3)
temp.add(19)
temp.add(40)
temp.add(25)
temp.printSelf()
print " "
print temp.isEmpty()
print " "
temp.appendWithTail(33)
temp.appendWithTail(2)
temp.printSelf()
temp.pop(1)
temp.printSelf()
print " "
temp.popEndOnly()
temp.printSelf()
print " "
temp.insert(4,10)
temp.printSelf()
print " "
temp.index(19)
temp.printSelf()
print " "
print " hi"
#######################

tempOrderedList = OrderedList()
tempOrderedList.addOrderedList(2)
tempOrderedList.printSelf()
tempOrderedList.addOrderedList(10)
tempOrderedList.printSelf()
tempOrderedList.addOrderedList(4)
tempOrderedList.printSelf()
tempOrderedList.addOrderedList(1)
tempOrderedList.printSelf()





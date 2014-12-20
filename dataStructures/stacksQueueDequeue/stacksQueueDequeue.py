from pythonds.basic.stack import Stack

def revstring(mystr):
    """ given a string, create another 
    string that reverses the word  """
    myStack = Stack() #create an instance of Stack class
    for ch in mystr: #given a string, iterate over of O(n)
        myStack.push(ch)  #add ch to the stack LIFO
    revstr = ' ' #create an empty string
    while not myStack.isEmpty(): #while myStack is not empty
        levstr = myStack.pop() # remove that last position of the stack
        revstr += levstr #add the word to the empty string
        
    return revstr #return the string that is being concated with
# strategy: if a list is not given, create a list and iterate over
#the string and append to the list
#create a new empty string, pop from the list, and pop returns the element
#add that element to the empty string, and return that as your answer

#there is no way to "pop()" a string, so this is a way around it.
#complexity: O(n)

def checkToSeeIfParanBalance(string):
    """ This is to check is the parantheses given in a string is balanced
    returns True or False..Complexity: O(n)"""
    
    stringStack = Stack()
    if len(string) == 0:
        return "String is empty"
    for ch in string: #we know the string length
        if ch == '(':  #identify the character
            stringStack.push(ch) #push it to the list
        elif len(string) == 0 and ch == ')':
            return False
        elif ch == ')' and len(string) > 0: #if it's the oppos. paran
            stringStack.pop() # remove the most recent (
        
        else:
            return "Only enter paraentheses"
    if stringStack.isEmpty(): #if you have an empty string at the end
        return True
    else:
        return False

#a common method to see if something is balanced, or print one instance 
#something is to iterate, see if they are =, then pop the item

def checkMultipleTypesBrackets(string):
    """ to check is (), {}, [] are balanced; O(n) complex. """
    stringStack = Stack()
    if len(string) == 0:
        return "String is empty"
    for ch in string: #we know the string length
        if ch in '({[':  #identify the character
            stringStack.push(ch) #push it to the list
        elif ch in '])}' and stringStack.isEmpty():
            return "error"
        else: #if it's the oppos. paran
            topCharacter = stringStack.pop() # remove the most recent (
            if not matches(topCharacter, ch):
                return False
        # else:
        #   return "Only enter paraentheses"
    if stringStack.isEmpty(): #if you have an empty string at the end
        return True
    else:
        return False

def matches(top, ch):
    tops = '([{'
    chs = ')]}'
    return tops.index(top) == chs.index(ch)

def convertingIntToBinary(num):
    stackInt = Stack()

    while num > 0:
        rem = num % 2 #gives you 1 or 0
        stackInt.push(rem) #add it to the stack
        num = num // 2 #divide by 2, until we get to 1, where while loops fails

    binString = " "

    while not stackInt.isEmpty():
        binString = binString + str(stackInt.pop())
    return binString

def convertDecToBase(decNum, base):
    digits = '0123456789ABCDEF'

    stack = Stack()

    while decNum > 0:
        print str(decNum) + " num"
        rem = decNum % base
        print str(rem) + " modulo"
        stack.push(rem)
        decNum = decNum // base
        print str(decNum) + "divide"
 
    string = " "

    while not stack.isEmpty():
        string = string + digits[stack.pop()]
    return string

# def infixPostfix(stringExpression):
#   prec = {}  #add the operators to the dictionary
#   prec['*'] = 3
#   prec['/'] = 3
#   prec['+'] = 2
#   prec['-'] = 2
#   prec['('] = 1

#   opStack = Stack() #create an instance of Stack
#   postfixList = [] #create list
#   tokenList = stringExpression.split() #split returns a list and breaks up string by each character
#   print tokenList
#   for token in tokenList:
#       print str(token) + " this is a token" 
#       if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
#           postfixList.append(token) #append characters in new list bc there could be operators;
#           #wants to separate operators from operands
#           print postfixList
#           print "this is the list"
#       elif token == '(':
#           opStack.push(token) #push ( to the stack, sep. from chars/nums
#       elif token == ')':
#           topToken = opStack.pop() #if you have a closing paran. pop most recent stack == (
#           while topToken != '(':
#               postfixList.append(topToken)
#               topToken = opStack.pop()
#       else:
#           while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
#               postfixList.append(opStack.pop())
#               print postfixList
#               print "this is the bottom of list"
#           opStack.push(token)

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split() # sep. each chara and put each char in a list

    print tokenList
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token) 
            print postfixList
            print "for loop"
        elif token == '(':
            opStack.push(token) #open ( append to stack
        elif token == ')':
            topToken = opStack.pop() #close ) remove the top of stack (which shoould have '(')
            print topToken
            print "elif before while"
            while topToken != '(': #if the stack is not open '('
                postfixList.append(topToken) #append what you popped '*+-/'
                print postfixList
                print "1st while"
                topToken = opStack.pop() #keep removing until '(' is reach which makes while = False
                print topToken
                print "while loop"
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]): #compare values from dic
                print prec[opStack.peek()]
                print prec[token]
                print "sec. while"
                postfixList.append(opStack.pop()) 
                
            opStack.push(token) #when while is false, push to stack

    while not opStack.isEmpty():
        postfixList.append(opStack.pop()) #if stack is not empty, append last item to list
        print postfixList
        print "last while"
    return " ".join(postfixList) #join list with spaces

print revstring('apple')
print revstring('x')
print checkToSeeIfParanBalance('((()()))') #True
print checkToSeeIfParanBalance('((())') #False
print checkMultipleTypesBrackets('((]') #False 
print checkMultipleTypesBrackets('()') #True
print convertingIntToBinary(4)
print convertDecToBase(256,16)
print " ----------"

print infixToPostfix("( A * B + C * D )")



# testEqual(revstring('apple'), 'elppa')
# testEqual(revstring('x'), 'x')
# testEqual(revstring('123456'), '654321')


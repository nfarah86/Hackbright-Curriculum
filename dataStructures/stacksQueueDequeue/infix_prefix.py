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
        return stack.pop()

    # def operator(self):
    #     return 1 if opr in ["+","-","*","/","^","$"] else 0

    # def operand(self):
    #     return 1 if(not(operator(self)) and (opr != "(") and (opr != ")")) else 0


    # def precedence(self):
    #     if((opr == "^") or (opr == "$")):return(7)
    #     if(opr == "*"):return(7)
    #     if(opr == "/"):return(7)
    #     if(opr == "+"):return(4)
    #     if(opr == "-"):return(4)
    #     #if(opr == "("):return(2)
    #     if(opr == ")"):return(1)

# Re-working infix-->prefix...

temp = Stack()
temp.push_stack('3') 
print temp.peek()
temp.push_stack('+') 
print temp.peek()
print temp.stack_top()
print temp.is_Empty()

#print temp.precedence()

# def infix_to_prefix(infix_expression):
#     print infix_expression
#     prefix_list = []
#     stack = []
#     lst = list(infix_expression)
#     lst = lst.reverse()
#     #infix_expression = infix_expression[::-1]
#     #infix_list = list(infix_expression)
#     #print lst
#     for i in lst:
#         if operand(i):
#             prefix_list.append(i)
#         if operator(i):
#             while((not(stack_empty(stack))) and (precedence(i) <= precedence(stack_top(stack)))):
#                 push_stack(stack, i)

#                 #prefix_list.append(stack_top(stack))
#                 #pop_stack(stack)
#                 #push_stack(stack,i)
#         if(i == ")"):
#             push_stack(stack,i)
#         if(i == "("):
#             while(stack_top(stack) != ")"):
#                 append_operator = pop_stack(stack)
#                 prefix_list.append(append_operator)
#             pop_stack(stack)
#     while(not(stack_empty(stack))):
#         if(stack_top(stack) == ")"):
#             pop_stack(stack)
#         else:
#             prefix_list.append(pop_stack(stack))
#     #print prefix_list       
#     prefix_expression = ''
#     for val in prefix_list:
#         prefix_expression += val

#     return prefix_expression[::-1]

# def main():
#     infix_expression = raw_input('\nEnter A Valid Expression (0-9 A-Z a-z + - / * ^ $) : ')
#     result = infix_to_prefix(infix_expression)
#     print 'Prefix of given expression: ', result

# main()
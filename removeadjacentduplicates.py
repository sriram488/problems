def remove_duplicates(s):
    stack = []
    for char in s:
         #check if stack is not empty and check if the top element of stack is same as the string character
        if stack and stack[-1] == char: 
             stack.pop() # if the condition is met pop the character from the stack
        else:
             stack.append(char) #push the char at the top
    return ''.join(stack)

print(remove_duplicates("abbaca")

def sol(c):
    stack = []
    lookup = {'[':']','(':')','{':'}'}
    for char in c:
        if char in lookup.keys():
            stack.append(lookup[char])
        elif stack and char == stack[-1]:
            stack.pop()
        else:
            return False
    
    return stack == [] 

c = '[][][][][][][][][][][][]'
r = sol(c)
print(r)


print(r)
# for char in p:
#     if char == '(' or char == '[' or char == '{':
#         stack.append(char)
#     else:
#         if char == ')' or char == ']' or char == '}':
#             stack.pop()
# print(stack)
# if len(stack) == 0:
#     print('True')
# else:
#     print('False')
 


stack = []
print(type(stack)) #list
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)

print(f"stack top {stack[-1]}")
stack.pop()
print(f"stack top after pop {stack[-1]}")
#Stack1 using collection moduel in dqueue

import collections
stack = collections.deque()
stack.append(20)
stack.append(50)
stack.append(14)
stack.append(22)
print(stack)
print("Top of the stack:",stack[-1])
stack.pop()
print(stack)
stack.pop()
print(stack)

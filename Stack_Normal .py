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

# In LIFOQueue is LAST IN FIRST OUT. an iteam is queue is adding 
# using PUT(iteam) method and To remove an element get(iteam) method.
import queue
stack = queue.LifoQueue(4)
stack.put(50)
stack.put(40)
stack.put(10)
stack.put(39)
#stack.put(80)
#print("Top of the Stack:",stack[-1])
a = stack.get()
print(a)
b = stack.get()
print(b)
c = stack.get()
print(c)

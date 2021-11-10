# Implement Stack using list
s = [] 

# Insert last
s.append('1')
s.append('2')
s.append('3')
s.append('4')
# print(s)

# Remove last
s.pop() 
s.pop() 
s.pop()
# print(s)

# Implement Stack using collection.deque
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.pop()
s.is_empty()
s.push(9)
s.push(34)
s.push(78)
s.push(12)
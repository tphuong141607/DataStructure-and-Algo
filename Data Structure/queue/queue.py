# Implement Queue using list
queue = []
queue.insert(0, 1)
queue.insert(0, 2)
queue.insert(0, 3)
queue.insert(0, 4)

# print(queue.pop())
# print(queue)

# Implement Queue using collection.deque
from collections import deque 

class Queue:
    def __init__(self):
        self.container = deque()
    
    def enqueue(self,val):
        self.container.appendleft(val)
        
    def dequeue(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.dequeue())
print(pq.size())
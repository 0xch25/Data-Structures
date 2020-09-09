'''
Implementation of Priority Queue
'''
from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 50))
q.put((1, 60))
q.put((3, 10))

print(q.get())
# check queue size
print('Items in queue :', q.qsize())

# check if queue is empty
print('Is queue empty :', q.empty())

# check if queue is full
print('Is queue full :', q.full())
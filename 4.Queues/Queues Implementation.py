'''
Implementation of Queue Data structure in Python3 using Lists
'''
class Queues:
    def __init__(self):
        self.s1=[] #Empty List

    def isEmpty(self):
        if len(self.s1)==0:
            return True
    def enQueue(self,data):
        self.s1.append(data)  #insert Element
        print("Element Inserted:",data)
    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        else:
            x=self.s1.pop(0)
            print("popped element is:",x)
    def peek(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            print("top element is:",self.s1[-1])
    def print(self):
        if self.isEmpty():
            print("Empty Queue..No element to print")
            return
        else:
            for num in self.s1:
                print(num,end=' ')
            print('')

q=Queues()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.print()
q.deQueue()
q.enQueue(40)
q.peek()
q.enQueue(50)
q.peek()
q.print()
q.deQueue()
q.deQueue()
q.print()
q.deQueue()
q.deQueue()
q.print()
q.deQueue()

'''
OUTPUT:
        Element Inserted: 10
        Element Inserted: 20
        Element Inserted: 30
        10 20 30 
        popped element is: 10
        Element Inserted: 40
        top element is: 40
        Element Inserted: 50
        top element is: 50
        20 30 40 50 
        popped element is: 20
        popped element is: 30
        40 50 
        popped element is: 40
        popped element is: 50
        Empty Queue..No element to print
        Empty Queue

'''


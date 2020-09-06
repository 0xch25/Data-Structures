'''
Implementation of Queues using Linked Lists
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isEmpty(self):
        return self.front==None

    def enQueue(self,data):
        newnode=Node(data)
        if self.rear==None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        self.front=self.front.next
        if(self.front==None):
            self.rear=None
    def print(self):
        if self.isEmpty():
            print("No Elements")
        else:
            cur=self.front
            while(cur):
                print(cur.data,end=' ')
                cur=cur.next
            print("")
    def peek(self):
        last=self.front
        while(last):
            if last.next==None:
                print("peek element:",last.data)
                return
            else:
                last=last.next

q=Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
print("The elements in Queue are:")
q.print()
q.deQueue()
print("The elements in Queue are:")
q.print()
q.peek()
q.enQueue(50)
q.peek()
print("The elements in Queue are:")
q.print()

'''
OUTPUT:
The elements in Queue are:
10 20 30 
The elements in Queue are:
20 30 
peek element: 30
peek element: 50
The elements in Queue are:
20 30 50 


'''

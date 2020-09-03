'''Implementation of Stacks [LIFO] Using Linked Lists'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head:
            return True
        return False

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
            return self.head.data
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.head is None:
            return None
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data

    def peak(self):
        return self.head.data

    def display(self):
        llist=self.head
        while(llist):
            print(llist.data,end=" ")
            llist=llist.next


s=Stack()
s.push(11)
s.push(22)
s.push(33)
s.push(44)
s.display()
print("")
s.pop()
s.display()
print(" ")
print(s.peak(),end=" ")



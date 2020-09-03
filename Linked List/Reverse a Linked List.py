'''
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        print("newnode inserted:",data)

    def print(self,head):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()


    def Reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

L = LinkedList()
L.insert(3)
L.insert(2)
L.insert(0)
L.insert(4)
L.insert(5)
L.print(L.head)
L.Reverse()
L.print(L.head)

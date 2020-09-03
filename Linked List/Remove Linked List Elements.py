'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
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
        if head==None:
            print("Empty List")
        while current:
            print(current.data,end=' ')
            current = current.next
        print()

    def RemoveEle(self,ele):
        while self.head and self.head.data == ele:
            self.head = self.head.next
        curr = self.head
        prev = curr
        while curr:
            if curr.data == ele:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return self.head


L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(2)
L.insert(0)
L.insert(4)
L.insert(5)
L.print(L.head)
L.RemoveEle(4)
L.print(L.head)
'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

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

    def removeNthFromEnd(self,head,n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

L = LinkedList()
L.insert(3)
L.insert(2)
L.insert(0)
L.insert(4)
L.insert(5)
print("Before deleting Nth Node:")
L.print(L.head)
L.removeNthFromEnd(L.head,3)
print("after deleting Nth Node:")
L.print(L.head)

'''
OUTPUT:
Before deleting Nth Node:
3 2 0 4 5 
after deleting Nth Node:
3 2 4 5 
'''
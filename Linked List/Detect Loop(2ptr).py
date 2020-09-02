'''
Given a linked list, determine if it has a cycle in it.
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


    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:

                return True
        return False


L = LinkedList()
L.insert(3)
L.insert(2)
L.insert(0)
L.insert(-4)
L.head.next.next.next.next=L.head.next #Create a Loop i.e last node will point to the first node
print(L.detectLoop())

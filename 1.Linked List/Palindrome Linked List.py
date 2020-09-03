'''
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true


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
        if self.head is None:
            print("Empty List")
        while current:
            print(current.data,end=' ')
            current = current.next
        print()

    def palindrome(self,head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node:
            if node.data != head.data:
                return False
            node = node.next
            head = head.next
        return True

L = LinkedList()
L.insert(1)
L.insert(2)
L.insert(2)
L.insert(1)
#L.insert(4)
#L.insert(5)
L.print(L.head)
print(L.palindrome(L.head))
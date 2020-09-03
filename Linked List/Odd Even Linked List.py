'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in-place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

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

    def oddEven(self,head):
        if not head:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(2)
L.insert(0)
L.insert(4)
L.insert(5)
L.print(L.head)
L.oddEven(L.head)
L.print(L.head)
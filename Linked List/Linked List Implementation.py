
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

    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print("node inserted at front:",new_node.data)

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next= prev_node.next
        prev_node.next = new_node
        print("the node inserted after given node {}  is :{}".format(prev_node.data,new_data))


    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        print("Node inserted at End is:",new_node.data)

    def print(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()


L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(5)
L.insert(6)
L.print()
L.insertFront(1)
L.print()
L.insertAfter(L.head,2)
L.print()
L.insertAfter(L.head.next.next.next.next.next,7)
L.print()
L.insertAtEnd(8)
L.print()

'''
Implementation of Doubly Linked List Delete Operation
Reference: https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def Insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def DeleteNode(self,dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next is not None:
            dele.next.prev = dele.prev
        if dele.prev is not None:
            dele.prev.next = dele.next
    def printList(self, node):
        #print("\nTraversal in forward direction")
        while (node is not None):
            print(node.data,end=' ')
            last = node
            node = node.next
        print("")
llist = DoublyLinkedList()
llist.Insert(15)
llist.Insert(6)
llist.Insert(7)
llist.Insert(1)
llist.Insert(4)
llist.Insert(8)
llist.printList(llist.head)
llist.DeleteNode(llist.head.next.next)
print("After Deletion:")
llist.printList(llist.head)

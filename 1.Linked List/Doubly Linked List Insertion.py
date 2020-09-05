'''
Implementation of Doubly Linked List Insert Operations
Reference: https://www.geeksforgeeks.org/doubly-linked-list/
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def InsertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def InsertAtTail(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def printList(self, node):
        #print("\nTraversal in forward direction")
        while (node is not None):
            print(node.data,end=' ')
            last = node
            node = node.next
        '''
            print("\nTraversal in reverse direction")
            while (last is not None):
                print(last.data)
                last = last.prev
        '''
llist = DoublyLinkedList()
llist.InsertFront(15)
llist.InsertAtTail(6)
llist.InsertFront(7)
llist.InsertFront(1)
llist.InsertAtTail(4)
llist.insertAfter(llist.head.next, 8)
llist.printList(llist.head)

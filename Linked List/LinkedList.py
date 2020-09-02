'''
Linked List Implementation
The Class Linked List contains the following functions:
    1.insert(): inserts the Node into the linked list
    2.insertFront(): insert the node at front i.e Head
    3.insertAfter(): insert the node after the given value
    4.insertAtEnd(): used to insert at the end of the Linked List
    5.tail(): returns the last node value
    6.print(): prints the Linked list in a single line
    7.length(): returns the length of the linked list
    8.getByIndex(): returns the value at the given indexed node
    9.addAtIndex(): add node at specified index position
    10.DeleteAtIndex(): Delete the Node at specified index
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

    def tail(self):
        last=self.head
        while last.next:
            last=last.next
        return last.data

    def print(self,head):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
        print()

    def length(self):
        count=0
        cur=self.head
        while(cur):
            cur=cur.next
            count+=1
        return count

    def getByIndex(self,index):
        if index<0 and index>self.length():
            return -1
        else:
            if index==0:
                return self.head.data
            elif index==self.length()-1:
                return self.tail()
            else:
                cur=self.head
                count=0
                while(cur):
                    if count==index:
                        return cur.data
                    cur=cur.next
                    count+=1
                return -1

    def addAtIndex(self,index,data):
        newnode=Node(data)
        if index==0:
            self.insertFront(data)
        elif index==self.length()-1:
            self.insertAtEnd(data)
        else:
            current = 0
            prev = None
            node = self.head
            newNode = Node(data)
            while current != index and node.next != None:
                prev = node
                node = node.next
                current += 1
            if current == index:
                prev.next = newNode
                newNode.next = node
            else:
                return -1
        print("The node inserted at given index {} is {}".format(index,data))

    def DeleteAtIndex(self,index):
        if index==0:
            temp=self.head.data
            Newhead=self.head.next
            self.head=Newhead
            return temp
        else:
            node=self.head
            cur=0
            prev=None
            while cur!=index and node.next:
                prev=node
                node=node.next
                temp=node.data
                cur+=1
            if cur==index:
                prev.next=node.next
            return temp



L = LinkedList()
L.insert(3)
L.insert(4)
L.insert(5)
L.insert(6)
L.print(L.head)
L.insertFront(1)
L.print(L.head)
L.insertAfter(L.head,2)
L.print(L.head)
L.insertAfter(L.head.next.next.next.next.next,7)
L.print(L.head)
L.insertAtEnd(8)
L.print(L.head)
print("The length of the Linked List is:",L.length())
print("The tail Node is:",L.tail())
print("The value at given index is:",L.getByIndex(4))
L.addAtIndex(4,10)
L.print(L.head)
print("The length of the Linked List is:",L.length())
print("The node deleted at given index is:",L.DeleteAtIndex(4))
L.print(L.head)
L.addAtIndex(6,10)
L.print(L.head)


'''
OUTPUT:
newnode inserted: 3
newnode inserted: 4
newnode inserted: 5
newnode inserted: 6
3 4 5 6 
node inserted at front: 1
1 3 4 5 6 
the node inserted after given node 1  is :2
1 2 3 4 5 6 
the node inserted after given node 6  is :7
1 2 3 4 5 6 7 
Node inserted at End is: 8
1 2 3 4 5 6 7 8 
The length of the Linked List is: 8
The tail Node is: 8
The value at given index is: 5
The node inserted at given index 4 is 10
1 2 3 4 10 5 6 7 8 
The length of the Linked List is: 9
The node deleted at given index is: 10
1 2 3 4 5 6 7 8 
The node inserted at given index 6 is 10
1 2 3 4 5 6 10 7 8 

'''
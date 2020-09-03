'''
program to find the Nth Node from The End of Linked List
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

#Approach1: find nth element from the end(find length)
    def findnth1(self, n):
        temp = self.head
        len = 0
        while temp:
            temp = temp.next
            len += 1
        if n > len:
            print("not possible")
        temp = self.head
        for i in range(0, len - n):
            temp = temp.next
        print("nth element is:")
        print(temp.data)

#Approach2: find nth from the end using 2 pointers
    def findnth2(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0
        if (self.head is not None):
            while (count < n):
                if (ref_ptr is None):
                    print("%d is greater than the no. of nodes in list"%(n))
                ref_ptr = ref_ptr.next
                count += 1
        while (ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        print(main_ptr.data)




L = LinkedList()
L.insert(3)
L.insert(2)
L.insert(0)
L.insert(-4)
print("Using 1st Approach")
L.findnth1(1)
print("Using 2nd Approach")
L.findnth2(3)

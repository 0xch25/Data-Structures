'''
Implementation of Binary Tree Using Linked list
'''
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data,end=' ')
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(0)
root.insert(20)
root.insert(25)
root.PrintTree()

'''
Output:
0 3 6 12 14 20 25
 
i.e        12
        6     14
      3          20
    0               25
'''
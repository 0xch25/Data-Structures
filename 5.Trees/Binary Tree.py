'''
Implementation of Binary Tree and its Operations
Functions:
            Insert():inserts the new node wrt Values
            Inorder():Prints the values of the tree via Inorder Traversal
            preorder():Prints the values of the tree via preorder Traversal
            postorder():Prints the values of the tree via postorder Traversal
            minValueNode(): returns the minimum value in the tree
            deleteNode(): Remove the given Node
            FindVal(): returns True if the value is present else False
            PrintTree(): it is similar to inorder traversal which prints the values in the tree
            Height():Returns the height of the root recursively

Reference:
            1.https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
            2.GeeksForGeeks.com
'''
class Node:
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key) 
    if key < node.key:
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.key, end=' ')
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root is not None:
        inorder(root.left)
        inorder(root.right)
        print(root.key, end=' ')

def minValueNode(node):
    current = node 
    while(current.left is not None):
        current = current.left  
    print("Min values is:",current.key)

def deleteNode(root, key):
    if root is None:
        return root  
    if key < root.key:
        root.left = deleteNode(root.left, key) 
    elif(key > root.key):
        root.right = deleteNode(root.right, key) 
    else:
        if root.left is None :
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right , temp.key)
    return root

def FindVal(root,val):
    if val<root.key:
        if root.left is None:
            return False
        return FindVal(root.left,val)
    elif val>root.key:
        if root.right is None:
            return False
        return FindVal(root.right,val)
    else:
        return True
def Height(root):
    if root is None:
        return -1
    lheight=Height(root.left)
    rheight=Height(root.right)
    return 1+max(lheight,rheight)

def PrintTree(root):
    if root.left:
        PrintTree(root.left)
    print(root.key,end=' ')
    if root.right:
        PrintTree(root.right)

""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  
root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80)
PrintTree(root)
print("\nInorder:")
inorder(root)
print("\npreorder:")
preorder(root)
print("\npostorder:")
postorder(root)
print("\nDelete 20")
root = deleteNode(root, 20) 
inorder(root)
print("\nDelete 30")
root = deleteNode(root, 30) 
#print(" ")
print(FindVal(root,80))
print(FindVal(root,10))
PrintTree(root)
print(" ")
minValueNode(root)
deleteNode(root,40)
minValueNode(root)
print("The Height of the tree is:",Height(root))


'''
OUTPUT:
20 30 40 50 60 70 80 
Inorder:
20 30 40 50 60 70 80 
preorder:
50 20 30 40 60 70 80 
postorder:
20 30 40 60 70 80 50 
Delete 20
30 40 50 60 70 80 
Delete 30
True
False
40 50 60 70 80  
Min values is: 40
Min values is: 50
The Height of the tree is: 2
'''
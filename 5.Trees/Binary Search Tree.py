'''
Implementation of Binary search Tree with its Basic Operations:
        inorder():prints the binary Tree
        insert(): Inserts the value
        minValueNode(): returns minimum value node (required for Node Deletion function
        PrintmaxValue(): prints the maximum value
        PrintminValue(): Prints the minimum value
        Delete(): Deletes the node
        search(): Search for value in iterative
        search2(): Search for value in Recursive

Reference: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
           https://github.com/careermonk/data-structures-and-algorithmic-thinking-with-python/blob/master/src/chapter06trees/BST.py
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def PrintmaxValue(node):
    cur=node
    while cur.right:
        cur=cur.right
    return cur.key
def PrintminValue(node):
    cur=node
    while cur.left:
        cur=cur.left
    return cur.key

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
#iterative
def search(root,val):
    cur=root
    while  cur:
        if val==cur.key:
            return True
        if val<cur.key:
            cur=cur.left
        else:
            cur=cur.right
    return False
#recursive
def search2(root,val):
    if root is None:
        return False
    if val<root.key:
        return search2(root.left,val)
    elif val>root.key:
        return search2(root.right,val)
    return True

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

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("\nInorder traversal of the modified tree")
inorder(root)
print("\nThe max value in given BST is:",PrintmaxValue(root))
print("The min value in given BST is:",PrintminValue(root))
print("Iterative Search:")
print(search(root,10))
print(search(root,80))
print("recursive search:")
print(search2(root,10))
print(search2(root,40))

'''
Output:
        Inorder traversal of the given tree
        20 30 40 50 60 70 80 
        Delete 20
        Inorder traversal of the modified tree
        30 40 50 60 70 80 
        Delete 30
        Inorder traversal of the modified tree
        40 50 60 70 80 
        Delete 50
        
        Inorder traversal of the modified tree
        40 60 70 80 
        The max value in given BST is: 80
        The min value in given BST is: 40
        Iterative Search:
        False
        True
        recursive search:
        False
        True
'''


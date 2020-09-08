'''
Program to Implement Level Order Traversal
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


def Height(root):
    if root is None:
        return -1
    lheight = Height(root.left)
    rheight = Height(root.right)
    return 1 + max(lheight, rheight)


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = Height(root)
    for i in range(1, h + 2):
        printGivenLevel(root, i)

# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.key, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

def PrintTree(root):
    if root.left:
        PrintTree(root.left)
    print(root.key, end=' ')
    if root.right:
        PrintTree(root.right)

'''
Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 
'''
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
PrintTree(root)
print("\nThe Height of the tree is:", Height(root))
print("The Level Order Traversal of given tree is:")
printLevelOrder(root)

'''
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left=Node(60)
root.right.right=Node(80)
'''

'''
OUTPUT:
20 30 40 50 60 70 80 
The Height of the tree is: 2
The Level Order Traversal of given tree is:
50 30 70 20 40 60 80 
'''
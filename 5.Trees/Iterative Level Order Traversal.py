
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

def levelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            temp = q.pop(0)
            print(temp.key,end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            count -= 1
def PrintTree(root):
    if root.left:
        PrintTree(root.left)
    print(root.key, end=' ')
    if root.right:
        PrintTree(root.right)

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
PrintTree(root)
print("\nThe Level Order Traversal of given tree is:")
levelOrder(root)

'''
OUTPUT:
20 30 40 50 60 70 80 
The Level Order Traversal of given tree is:
50 30 70 20 40 60 80 
'''
'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
'''


def rangeSumBST(root, L, R):
    if root is None:
        return 0
    if root.val > R:
        return rangeSumBST(root.left, L, R)
    if root.val < L:
        return rangeSumBST(root.right, L, R)
    return root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)
root = [10,5,15,3,7,None,18]
L = 7
R = 15
print(rangeSumBST(root,L,R))
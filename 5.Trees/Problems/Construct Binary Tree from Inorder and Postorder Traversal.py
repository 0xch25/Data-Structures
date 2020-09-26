'''
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(inorder, postorder):
        def helper(left,right):
                    if left > right:
                        return None
                    val = postorder.pop()
                    root = TreeNode(val)
                    index = inorderValToIdx[val]
                    root.right = helper(index +1, right)
                    root.left = helper(left,index-1)
                    return root
        inorderValToIdx = {val:idx for idx, val in enumerate(inorder)}
        return helper(0,len(inorder)-1)
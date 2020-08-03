'''
Search in a Binary Search Tree

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        while current != None:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
                continue
            else:
                current = current.right
                continue
        return 
                

#Runtime: 72 ms
#Memory Usage: 15.8 MB
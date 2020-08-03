'''
Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def countNodes(self, root):
        count = 0
        while root:
            l, r = map(self.getHeight, (root.left, root.right))
            count += 2 ** r
            root = root.right if l==r else root.left
        return count
    
#Runtime: 80 ms
#Memory Usage: 21.2 MB
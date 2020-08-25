'''
Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(node, isLeft):
            if node:
                if isLeft and not node.left and not node.right:
                    return node.val # Only returns when isLeft and isLeaf
                return helper(node.left, True) + helper (node.right, False)
            return 0
        return helper(root, False) # Seems that the OJ doesn't treat bare root as a left leaf

#Runtime: 36 ms
#Memory Usage: 14.5 MB
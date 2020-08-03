''' 
Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
''' 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        q = [(root, 1)]
        ans = 1 
        while q:
            if len(q) >= 2:
                ans = max(q[-1][1] - q[0][1] + 1, ans)
            new_q = []
            while q:
                node, pos = q.pop(0)                      
                if node.left: new_q.append((node.left, 2*pos))
                if node.right: new_q.append((node.right, 2*pos + 1))            
            q = new_q
        return ans

#Runtime: 40 ms
#Memory Usage: 14.2 MB

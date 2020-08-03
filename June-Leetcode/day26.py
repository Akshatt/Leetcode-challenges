'''
Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            new_value = value*10+root.val
            self.dfs(root.left, new_value)
            self.dfs(root.right, new_value)
            if not root.left and not root.right:
                self.res += new_value

#Runtime: 24 ms
#Memory Usage: 14.1 MB
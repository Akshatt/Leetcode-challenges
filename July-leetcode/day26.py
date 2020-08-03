'''
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.addLevel(ans, 0, root)
        return ans
        
    def addLevel(self, ans, level, root):
        if not root:
            return
        elif len(ans) <= level:
                ans.append([root.val])
        elif not level%2:
            ans[level].extend([root.val])
        else:
            ans[level].insert(0,root.val)
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)

#Runtime: 36 ms
#Memory Usage: 14.1 MB
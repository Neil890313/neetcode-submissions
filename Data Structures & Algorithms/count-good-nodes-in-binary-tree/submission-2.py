# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        # top down
        def dfs(node, prev):
            if not node:
                return
            if node.val >= prev:
                self.ans += 1

            left = dfs(node.left, max(prev, node.val))
            right = dfs(node.right, max(prev, node.val))
        dfs(root, root.val)
        return self.ans

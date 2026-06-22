# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxSoFar = root.val
        def dfs(node, maxSoFar):
            tmp = 0
            if not node:
                return 0
            if node.val >= maxSoFar:
                tmp = 1
            maxSoFar = max(maxSoFar, node.val)
            left = dfs(node.left, maxSoFar)
            right = dfs(node.right, maxSoFar)

            return left + right + tmp
        return dfs(root, maxSoFar)


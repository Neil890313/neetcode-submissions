# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def dfs(node):
            # or self.ans is not None
            token = False
            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                token = True
            
            left = dfs(node.left)
            right = dfs(node.right)

            if (left and right) or (token and left) or (token and right):
                self.ans = node

            return left or right or token

        dfs(root)
        return self.ans
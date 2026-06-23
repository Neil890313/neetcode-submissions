# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.ans= None

        def dfs(root):
            if not root or self.ans is not None:
                return
            dfs(root.left)

            if self.ans is None:
                if self.count == k:
                    self.ans = root.val
                    return 
                self.count += 1

            dfs(root.right)

        dfs(root)

        return self.ans
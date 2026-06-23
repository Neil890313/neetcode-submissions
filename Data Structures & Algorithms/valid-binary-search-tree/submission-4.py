# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.token = True

        def dfs(root):
            if not root:
                return
            dfs(root.left)

            if self.prev is not None:
                if self.prev >= root.val:
                    self.token = False
            self.prev = root.val

            dfs(root.right)
             
        dfs(root)

        return self.token
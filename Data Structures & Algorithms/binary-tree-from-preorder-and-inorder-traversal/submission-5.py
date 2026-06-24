# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        self.index = 0

        def helper(start, end):
            if start > end:
                return None
            
            # Find root
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            # split left and right
            mid = idx_map[root_val]
            # [順序重要!!] preorder 的順序為 root -> left -> right，所以先左再右
            root.left = helper(start, mid-1)
            root.right = helper(mid+1, end)

            return root
        return helper(0, len(inorder)-1)
            

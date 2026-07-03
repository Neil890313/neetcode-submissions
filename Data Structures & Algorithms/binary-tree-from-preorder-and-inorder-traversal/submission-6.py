# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        idx_map = {}
        for idx, value in enumerate(inorder):
            idx_map[value] = idx

        def dfs(left, right):
            if left > right:
                return 
            root_val = preorder[self.idx]
            self.idx += 1
            root = TreeNode(root_val)

            inorder_idx = idx_map[root_val]
            left_tree = dfs(left, inorder_idx-1)
            right_tree = dfs(inorder_idx+1, right)
            root.left = left_tree
            root.right = right_tree

            return root

        return dfs(0, len(inorder)-1)




            

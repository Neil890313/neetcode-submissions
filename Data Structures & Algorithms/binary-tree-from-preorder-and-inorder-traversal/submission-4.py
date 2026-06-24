# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx_dict = {}
        for idx, value in enumerate(inorder):
            self.idx_dict[value] = idx

        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            left_tree_size = self.idx_dict[root_val] - in_l

            root.left = dfs(pre_l + 1, pre_l +  left_tree_size, in_l, in_l + left_tree_size)
            root.right = dfs(pre_l + left_tree_size +1, pre_r, in_l + left_tree_size + 1, in_r)
            return root
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
            

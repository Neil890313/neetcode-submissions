# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_dict = {v: i for i, v in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            # 沒有 node 的情況
            if pre_l > pre_r:
                return None
            # 找出 root，以及在 inoerder 上的位置 
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            root_idx = idx_dict[root_val]

            # 左樹的大小，用以圈出下一個迴圈的範圍
            left_size = root_idx - in_l
            
            root.left = build(pre_l+1, pre_l+left_size, in_l, root_idx-1)
            root.right = build(pre_l + left_size + 1, pre_r, root_idx + 1, in_r)
            return root
        
        return build(0, len(preorder)-1, 0, len(inorder))
            

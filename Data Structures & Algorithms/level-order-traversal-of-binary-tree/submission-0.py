# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)

                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
            ans.append(tmp)
        return ans
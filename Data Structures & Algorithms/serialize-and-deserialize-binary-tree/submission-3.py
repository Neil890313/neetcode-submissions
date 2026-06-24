# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ans = []

        def dfs(node):
            if not node:
                self.ans.append("#")
                return

            self.ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(self.ans)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        
        self.index = 0

        def dfs():
            if self.index == len(data):
                return

            root_val = data[self.index]
            self.index += 1
            
            if root_val == "#":
                return 
            root = TreeNode(int(root_val))
            

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


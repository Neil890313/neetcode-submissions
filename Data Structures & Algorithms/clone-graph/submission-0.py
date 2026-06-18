"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        old2new = {None:None}
        q = deque()
        q.append(node)
        visited = set()
        visited.add(node)

        while q:
            for _ in range(len(q)):
                tmp = q.popleft()
                old2new[tmp] = Node(tmp.val)
                for n in tmp.neighbors:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
        q = deque()
        q.append(node)
        visited = set()
        visited.add(node)

        while q:
            for _ in range(len(q)):
                tmp = q.popleft()
                clone = old2new[tmp]
                for n in tmp.neighbors:
                    clone.neighbors.append(old2new[n])
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
                        

        return old2new[node]
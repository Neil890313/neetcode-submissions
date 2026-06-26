class Solution:
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return True
        if self.rank[rb] > self.rank[ra]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parents = list(range(n))
        self.rank = [0]*n

        for u, v in edges:
            u, v = u-1, v-1
            token = self.union(u, v)
            if token:
                return [u+1, v+1]


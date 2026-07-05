class Solution:
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return True
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = list(range(len(edges)))
        self.rank = [0]*len(edges)

        for u, v in edges:
            if self.union(u-1, v-1):
                return [u, v]



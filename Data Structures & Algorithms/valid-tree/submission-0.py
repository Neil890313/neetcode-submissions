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
        if self.rank[rb] == self.rank[ra]:
            self.rank[ra] += 1
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.parents = list(range(n))
        self.rank = [0]*n

        for u, v in edges:
            token = self.union(u, v)
            if token:
                return False
        return len({self.find(i) for i in range(n)}) == 1
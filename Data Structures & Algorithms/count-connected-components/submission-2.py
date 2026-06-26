class Solution:
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        elif self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = list(range(n))
        self.rank = [0]*n

        for u, v in edges:
            self.union(u, v)

        # 目前 parents 其實已經全部連線完畢了，但是parents 中仍可能存在中間老大而不是最終老大

        return len({self.find(i) for i in range(n)})

        
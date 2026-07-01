class Solution:
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        # 兩者在同一個 Boss 之下
        if ra == rb:
            # 合併失敗
            return False
        if self.rank[rb] > self.rank[ra]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parents = list(range(n))
        self.rank = [0]*n

        for u, v in edges:
            token = self.union(u-1, v-1)
            if not token:
                return [u, v]


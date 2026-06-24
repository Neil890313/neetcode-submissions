class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## BFS
        # ans = 0
        # rows = len(grid)
        # cols = len(grid[0])
        # directions = [
        #     (0, -1), (-1, 0), (0, 1), (1, 0)
        # ]

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             ans += 1
        #             q = deque()
        #             q.append((r, c))
        #             grid[r][c] = "#"

        #             while q:
        #                 for _ in range(len(q)):
        #                     node = q.popleft()

        #                     for d in directions:
        #                         dx = node[0] + d[0]
        #                         dy = node[1] + d[1]

        #                         if 0<= dx < rows and 0 <= dy < cols and grid[dx][dy] == "1":
        #                             grid[dx][dy] = "#"
        #                             q.append((dx, dy))
        # return ans
        # DFS
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        def dfs(r, c):
            if r <0 or r>= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            for d in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                dfs(r+d[0], c+d[1])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)

        return ans

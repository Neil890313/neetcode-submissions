class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (-1,0), (0, -1), (1, 0), (0, 1)
        ]

        ## BFS
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             tmp_area = 1
                    
        #             q = deque()
        #             q.append((r, c))
        #             grid[r][c] = "#"

        #             while q:
        #                 for _ in range(len(q)):
        #                     node = q.popleft()

        #                     for d in directions:
        #                         dx = node[0] + d[0]
        #                         dy = node[1] + d[1]

        #                         if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
        #                             tmp_area += 1
        #                             grid[dx][dy] = "#"
        #                             q.append((dx, dy))
        #             ans = max(ans, tmp_area)
        # return ans
        # DFS
        def dfs(r, c):
            if r<0 or r>= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = "#"
            area = 1
            for d in directions:
                area += dfs(r+d[0], c+d[1])
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        return ans

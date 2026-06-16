class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    ans += 1
                    q = deque()
                    grid[r][c] = "*"
                    q.append((r, c))

                    while q:
                        for i in range(len(q)):
                            node = q.popleft()
                            for d in directions:
                                dx = node[0] + d[0]
                                dy = node[1] + d[1]
                                if 0 <= dx < rows and 0<= dy < cols and grid[dx][dy] == "1":
                                    grid[dx][dy] = "*"
                                    q.append((dx, dy))
        return ans


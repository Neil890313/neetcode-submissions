class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        count = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for d in directions:
                    dx = node[0] + d[0]
                    dy = node[1] + d[1]
                    if 0<= dx < rows and 0<= dy < cols and grid[dx][dy] == 2147483647:
                        grid[dx][dy] = count
                        q.append((dx, dy))
            count += 1
                


        

        



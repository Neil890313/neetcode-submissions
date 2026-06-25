class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        count = 0

        while q:
            if count >0:
                minutes += 1
            count+=1
            for _ in range(len(q)):
                node = q.popleft()

                for d in directions:
                    dx = node[0] + d[0]
                    dy = node[1] + d[1]
                    if 0 <= dx < rows and 0<= dy < cols and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        q.append((dx, dy))
        token = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    token = True
        return -1 if token else minutes

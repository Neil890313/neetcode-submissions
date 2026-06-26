class Solution:
    
    def __init__(self):
        # 建立實例變數，讓所有方法都能共用
        self.heights = []
        self.rows = 0
        self.cols = 0

    def bfs(self, q: deque, visited: set):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        while q:
            node = q.popleft()
            r, c = node[0], node[1]
            
            for d in directions:
                dx, dy = r + d[0], c + d[1]
                
                # 檢查邊界，並且確保 (dx, dy) 尚未被訪問過
                if 0 <= dx < self.rows and 0 <= dy < self.cols and (dx, dy) not in visited:
                    # 水往高處流 (因為我們是從海洋往陸地反向找)
                    if self.heights[dx][dy] >= self.heights[r][c]:
                        visited.add((dx, dy))
                        q.append((dx, dy))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.rows = len(heights)
        self.cols = len(heights[0])
        
        pacific_q = deque()
        pacific_visited = set()
        atlantic_q = deque()
        atlantic_visited = set()

        for r in range(self.rows):
            for c in range(self.cols):
                if r == 0 or c == 0:
                    pacific_q.append((r, c))
                    pacific_visited.add((r, c))
                    
        for r in range(self.rows):
            for c in range(self.cols):
                if r == self.rows-1 or c == self.cols-1:
                    atlantic_q.append((r, c))
                    atlantic_visited.add((r, c))

        self.bfs(pacific_q, pacific_visited)
        self.bfs(atlantic_q, atlantic_visited)

        return list(pacific_visited & atlantic_visited)





        
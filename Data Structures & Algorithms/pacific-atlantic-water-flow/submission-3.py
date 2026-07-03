class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        def bfs(queue, visited):
            directions = [
                (-1, 0), (0, -1), (1, 0), (0, 1)
            ]
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for d in directions:
                        dx = node[0] + d[0]
                        dy = node[1] + d[1]
                        if 0 <= dx < rows and 0 <= dy < cols and heights[dx][dy] >= heights[node[0]][node[1]]:
                            if (dx, dy) not in visited:
                                visited.add((dx, dy))
                                queue.append((dx, dy))
            return visited
        
        # pacific
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    q.append([r, c])
                    visited.add((r, c))
        pacific = bfs(q, visited)
        # atlantic
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if r == rows-1 or c == cols-1:
                    q.append([r, c])
                    visited.add((r, c))
        atlantic = bfs(q, visited)

        return list(pacific & atlantic)


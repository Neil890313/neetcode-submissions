class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 跟其他 Grid 的做法一樣，只是只需要抓 O 在 邊上的做 BFS 即可

        rows = len(board)
        cols = len(board[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]

        # BFS
        # for r in range(rows):
        #     for c in range(cols):
        #         # [關鍵] 只抓在邊界上的 O 做 BFS 
        #         # () 內的便是判斷是否在邊界上
        #         if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == "O":
        #             q = deque()
        #             q.append((r, c))
        #             board[r][c] = "#"
        #             while q:
        #                 for _ in range(len(q)):
        #                     node = q.popleft()

        #                     for d in directions:
        #                         dx = d[0] + node[0]
        #                         dy = d[1] + node[1]
        #                         if 0<= dx < rows and 0 <= dy < cols and board[dx][dy] == "O":
        #                             board[dx][dy] = "#"
        #                             q.append((dx, dy))

        # DFS
        def dfs(r, c):
            if r<0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "#"
            for d in directions:
                dfs(r+d[0], c+d[1])

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == "O":
                    dfs(r,c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
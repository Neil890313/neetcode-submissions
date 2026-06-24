class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]

        def dfs(r, c , i):
            # 找完了
            if i == len(word):
                return True
            # 死路
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            i += 1

            for d in directions:
                token = dfs(r+d[0], c+d[1], i)
                if token:
                    break
            board[r][c] = tmp

            return token

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
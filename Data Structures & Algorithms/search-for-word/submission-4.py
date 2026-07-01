class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]
        # i 表示目前找到 word 中的第幾個字母
        def backtrace(r, c, i):
            # 找完
            if i == len(word):
                return True
            # 超出 board 或是找錯
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            # 找對
            tmp = board[r][c] 
            board[r][c] = "#"

            token = False
            for d in directions:
                token = backtrace(r+d[0], c+d[1], i+1)
                if token:
                    break
            board[r][c] = tmp
            return token

        for r in range(rows):
            for c in range(cols):
                token = backtrace(r, c, 0)
                if token:
                    return True
        return False

            

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        distences = [
            (-1, 0), (0, -1), (1, 0), (0, 1)
        ]

        def backtrace(r, c, index):
            if index == len(word):
                return True
            elif r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            now = board[r][c]
            board[r][c] = "#"

            for d in distences:
                token = backtrace(r+d[0], c+d[1], index+1)
                if token:
                    return True
            board[r][c] = now

        for r in range(rows):
            for c in range(cols):
                token = backtrace(r, c, 0)
                if token:
                    return True
        return False 
            



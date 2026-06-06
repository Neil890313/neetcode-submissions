class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = collections.defaultdict(set)
        column_dict = collections.defaultdict(set)
        box_dict = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_id = (i//3, j//3)

                if board[i][j] in row_dict[i] or board[i][j] in column_dict[j] or board[i][j] in box_dict[box_id]:
                    return False

                row_dict[i].add(board[i][j])
                column_dict[j].add(board[i][j])
                box_dict[box_id].add(board[i][j])

        return True
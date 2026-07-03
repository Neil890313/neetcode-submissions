class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        # r-c
        diag1 = set()
        # r+c
        diag2 = set()

        def backtrace(row):
            # 收集路徑
            if len(path) == n:
                now_grid = []
                for i in path:
                    tmp = ["." for _ in range(n)]
                    tmp[i] = "Q"
                    now_grid.append("".join(tmp))
                res.append(now_grid)

            for col in range(n):
                ## 加入選項 
                # vertically check
                if col in path:
                    continue
                # diagonally check
                if row - col in diag1:
                    continue
                if row + col in diag2:
                    continue
                path.append(col)
                diag1.add(row-col)
                diag2.add(row+col)

                # dfs
                backtrace(row+1)

                # 撤銷選項
                path.pop()
                diag1.remove(row-col)
                diag2.remove(row+col)

        backtrace(0)
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        # 左上到右下: r-c 相同
        diag1 = set()
        # 左下到右上: r+c 相同
        diag2 = set()

        def backtrace(row):
            # 收集答案
            if len(path) == n:
                tmp_grid = []
                for i in path:
                    now = ["." for i in range(n)]
                    now[i] = "Q"
                    tmp_grid.append("".join(now))
                res.append(tmp_grid)  
                return                  

            for col in range(n):
                # 加入線索
                # vertically 確認
                if col in path:
                    continue
                # diagonally check
                if row-col in diag1:
                    continue
                # diagonally check
                if row+col in diag2:
                    continue
                path.append(col)
                diag1.add(row-col)
                diag2.add(row+col)
                # dfs
                backtrace(row+1)
                # 撤銷線索
                path.pop()
                diag1.remove(row-col)
                diag2.remove(row+col)
            

        backtrace(0)
        return res


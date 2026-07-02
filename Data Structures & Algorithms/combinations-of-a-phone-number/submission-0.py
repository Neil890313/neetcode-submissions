class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2char = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        res = []
        path = []

        def backtrace(idx):
            # now = num2char[int(digits[idx])]
            # 收集條件
            if len(path) == len(digits):
                res.append("".join(path))
                return
            now = num2char[int(digits[idx])]
            for i in range(len(now)):
                # 加入選項
                path.append(now[i])
                # dfs
                backtrace(idx+1)
                # 撤銷選項
                path.pop()


        backtrace(0)
        return res
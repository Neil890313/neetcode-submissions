class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []


        def is_palindrome(string):
            l = 0
            r = len(string)-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        # 用一個 start 參數(代表「目前切到 s 的第幾個字元了」)
        def backtrace(start):
            # 收集條件:全部字母都用到
            if start == len(s):
                res.append(path[:])

            # 展開決策樹
            for i in range(start, len(s)):
                # 增加選項
                # 判斷是否為回文
                substr = s[start:i+1]
                if not is_palindrome(substr):
                    continue
                path.append(substr)
                # dfs
                backtrace(i+1)
                # 撤銷選項
                path.pop()

        backtrace(0)
        return res
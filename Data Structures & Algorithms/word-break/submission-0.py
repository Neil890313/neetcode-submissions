class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is 到 s[:i]能不能用 worddict 中的word 組合出來
        dp = [False]*(len(s)+1)

        # base case 
        dp[0] = True
        # range
        for i in range(1, len(s)+1):
            # transfer logic
            for word in wordDict:
                # 將 s[:i] 分成兩個部分
                # 第一部分(後半) 找出長度跟 word 一樣，看看他等不等於 word 
                # 第二部分(前半) 移除後半後，dp[剩下的部分] 也要是 True
                if i >= len(word) and s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break

        # answer
        return dp[len(s)]
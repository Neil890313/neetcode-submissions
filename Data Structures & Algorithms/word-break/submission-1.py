class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)

        # base case
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if len(word) <= i and s[i-len(word): i] == word and dp[i-len(word)]:
                    dp[i] = True
                    break
        return dp[n]
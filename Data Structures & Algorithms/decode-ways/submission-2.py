class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]
        n = len(s)
        dp = [0]*(n+1)
        # base case 
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        # range
        for i in range(2, n+1):
            # transfer logic
            if 10 <= int(s[i-2:i]) <= 26 and dp[:i-2] != 0:
                dp[i] += dp[i-2]
            if s[i-1] != '0' and dp[:i-1] != 0:
                dp[i] += dp[i-1]
        # answer
        return dp[n]
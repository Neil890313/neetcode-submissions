class Solution:
    def climbStairs(self, n: int) -> int:
        # What is status dp[i]?
        # It is the method that i can have
        dp = [0]*(n+1)
        # Base case ?
        dp[0], dp[1] = 1, 1
        # How many steps?
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
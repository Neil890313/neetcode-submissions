class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # status?
        # dp[i] is the cost to i so far
        n = len(cost)
        dp = [0]*(n+1)
        # base case?
        # we can start from idx 0 or 1, so it don't cost anything
        dp[0], dp[1] = 0, 0
        # iterative?
        for i in range(2, n+1):
            # In idx i, we have two possibilitiy, start from idx-2 or idx-1
            # with there cost so they can reach idx i
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n]

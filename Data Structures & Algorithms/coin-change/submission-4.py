class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 要累積到 i 最少需要多少硬幣
        dp = [float('inf')]*(amount+1)

        # base case 
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin]+1, dp[i])

        return -1 if dp[amount] == float('inf') else dp[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is the least number of coins we need to achieve i
        dp = [float('inf')]*(amount+1)
        # base case
        dp[0] = 0

        # range
        for i in range(1, amount+1):
            # transfer logic
            # minus the coin that need to add, how many coins we need to achieve the rest
            for coin in coins:
                # boundary
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # answer
        return -1 if dp[amount] == float('inf') else dp[amount]
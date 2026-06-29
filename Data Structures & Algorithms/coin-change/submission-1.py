class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        # base case
        dp[0] = 0                                  
        for i in range(1, amount + 1):
            for coin in coins:
                # ← 補上邊界:金額夠才放
                if i - coin >= 0:                  
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]
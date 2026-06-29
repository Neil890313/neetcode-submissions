class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0                                  # base case
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:                  # ← 補上邊界:金額夠才放
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]
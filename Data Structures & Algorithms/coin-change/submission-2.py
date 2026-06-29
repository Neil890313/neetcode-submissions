class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 為要累積到 i 最少的硬幣數量
        # 因為要求要最少，所以初始是一個極大值
        dp = [float('inf')]*(amount+1)

        # base case
        # 0 不需要硬幣 
        dp[0] = 0
        # range
        for i in range(1, amount+1):
            # transfer logic
            for coin in coins:
                # 確保不為負數
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] == float('inf') else dp[amount] 
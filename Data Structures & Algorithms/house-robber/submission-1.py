class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp[i] 為「考慮前 i+1 間房子(第 0 到第 i 間)、能搶到的最大金額」
        n = len(nums)
        dp = [0]*n

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            # 在 i 時，我有哪些選項
            # 1. 搶：現在這一家的錢加上 i-2 家前能搶到的最多錢
            # 2. 不搶：i-1 家前能搶到的最多錢
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[n-1]
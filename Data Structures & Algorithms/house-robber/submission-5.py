class Solution:
    def rob(self, nums: List[int]) -> int:
        # status?
        # dp[i] means that at idx i how much money we got so far
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n

        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # two options
            # 1. rob i,then we can get nums[i], and have the money from dp[i-2]
            # 2. don't rob i, then we can choose dp[i-1]
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[n-1]
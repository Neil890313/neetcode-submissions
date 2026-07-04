class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] means 在 i 這個位置目前有的最多財富
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n

        # base case 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[n-1]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] is (min, max) 
        n = len(nums)
        dp = [(0, 0)]*n
        dp[0] = (nums[0], nums[0])
        ans = nums[0]

        for i in range(1, n):
            prev_min = dp[i-1][0]
            prev_max = dp[i-1][1]
            if nums[i] < 0:
                prev_max, prev_min = prev_min, prev_max
            dp[i] = (
                min(nums[i], nums[i]*prev_min),
                max(nums[i], nums[i]*prev_max)
            )
            ans = max(ans, dp[i][1])

        return ans
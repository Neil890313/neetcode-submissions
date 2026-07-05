class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[float('inf'), float('-inf')]]*n
        ans = nums[0]

        # base case
        dp[0] = [nums[0], nums[0]]

        for i in range(1, n):
            prev_min, prev_max = dp[i-1][0], dp[i-1][1]

            if nums[i] < 0:
                prev_min, prev_max = prev_max, prev_min
            dp[i] = [
                min(nums[i], nums[i]*prev_min),
                max(nums[i], nums[i]*prev_max)
            ]
            ans = max(ans, dp[i][1])
        return ans
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] is the min and the max at i
        n = len(nums)
        dp = [(0, 0)]*n
        ans = nums[0]
        # base case
        dp[0] = (nums[0], nums[0])

        for i in range(1, n):
            prev_min = dp[i-1][0]
            prev_max = dp[i-1][1]
            if nums[i] < 0:
                prev_min, prev_max = prev_max, prev_min
            dp[i] = (
                min(prev_min*nums[i], nums[i]),
                max(prev_max*nums[i], nums[i])
            )
            ans = max(ans, dp[i][1])
        return ans
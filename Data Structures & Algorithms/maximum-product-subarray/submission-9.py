class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(nums[0], nums[0])]*n
        ans = nums[0]

        for i in range(1, n):
            min_num = dp[i-1][0]
            max_num = dp[i-1][1]

            if nums[i] < 0:
                min_num, max_num = max_num, min_num
            dp[i] = (
                min(nums[i], min_num*nums[i]),
                max(nums[i], max_num*nums[i])
            )
            ans = max(ans, dp[i][1])
        return ans

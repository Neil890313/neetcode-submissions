class Solution:
    def rob(self, nums: List[int]) -> int:
        # 當下這個 i 累積的最多的錢
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n

        # base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(
                nums[i] + dp[i-2],
                dp[i-1]
            )
        return dp[n-1]


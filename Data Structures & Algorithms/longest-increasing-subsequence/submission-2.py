class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is the length of the longest subsequence at i
        n = len(nums)
        dp = [1]*n
        ans = 1

        # base case is 1 
        # range
        for i in range(1,n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(ans, dp[i])
        return ans
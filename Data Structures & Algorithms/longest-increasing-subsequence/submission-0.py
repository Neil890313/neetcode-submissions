class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # status
        # dp[i] 為以 i 為結尾的最常 subsequence 的長度
        n = len(nums)
        dp = [1]*n
        # base case 為 dp[0] = 1
        # range 為 1:n
        # 轉移邏輯
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
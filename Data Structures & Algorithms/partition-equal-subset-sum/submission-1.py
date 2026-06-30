class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total//2

        if total%2 == 1:
            return False

        dp = [False]*(half+1)
        # base case
        dp[0] = True

        # 0/1背包問題，反過來
        for num in nums:
            for i in range(half, num-1, -1):
                if dp[i-num]:
                    dp[i] = True

        return dp[half]


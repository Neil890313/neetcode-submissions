class Solution:
    def rob(self, nums: List[int]) -> int:
        # When it have cycle in dp,it can seperate it into two linear problem
        # 1. If don't rob i, then the houses we can rob is 1:n
        # 1. If don't rob n-1, then the houses we can rob is 0:n-1
        total_n = len(nums)
        if total_n == 1:
            return nums[0]
        def rob_linear(houses):
            n = len(houses)
            if n == 1:
                return houses[0]
            dp = [0]*n

            # base case 
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + houses[i], dp[i-1])
            return dp[n-1]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
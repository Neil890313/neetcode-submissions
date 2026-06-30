class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp[i] is the money we can get the most at ith
        
        def rob_linear(houses):
            n = len(houses)
            if n == 1:
                return houses[0]
            dp = [0]*n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, n):
                dp[i] = max(houses[i]+dp[i-2], dp[i-1])

            return dp[n-1]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1])) 


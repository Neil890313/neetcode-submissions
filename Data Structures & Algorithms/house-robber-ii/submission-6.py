class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def linear_rob(house):
            local_n = len(house)
            if local_n == 1:          # 補這行:子陣列只剩 1 間時
                return house[0]
            dp = [0]*local_n

            # base case 
            dp[0] = house[0]
            dp[1] = max(house[0], house[1])

            for i in range(2, local_n):
                dp[i] = max(
                    dp[i-1],
                    dp[i-2] + house[i]
                )
            return dp[local_n-1]
        return max(
            linear_rob(nums[1:]),
            linear_rob(nums[:-1])
        )
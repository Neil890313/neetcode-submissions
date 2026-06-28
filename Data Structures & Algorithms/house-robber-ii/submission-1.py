class Solution:
    def rob(self, nums: List[int]) -> int:
        # 遇到迴圈型的問題時，可以拆成兩條線性後比較
        # 情況一：不搶0，則可搶的房子 range 為 1:n-1
        # 強況二：不搶 n-1，則可搶的房子 range 為 0:n-2
        total_n = len(nums)
        if total_n == 1:
            return nums[0]

        def rob_line(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            n = len(houses)
            # 建置 dp notebook
            dp = [0]*n
            # base case
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            return dp[n-1]

        return max(rob_line(nums[1:total_n]), rob_line(nums[:total_n-1]))
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        # base case 
        dp[0] = (nums[0], nums[0])

        # [重要]最後一格不一定有最大值，因此需要全域變數持續紀錄
        ans = nums[0]

        # 移轉
        for i in range(1, n):
            # 兩種選擇
            # 1. 承接之前的結果 dp[i-1]*nums[i]
            # 2. 重新開始 nums[i]
            # [重點]負數會造成兩極反轉，最大的乘上負數會變最小；反之
            prev_min = dp[i-1][0]
            prev_max = dp[i-1][1]
            if nums[i] < 0:
                prev_min, prev_max = prev_max, prev_min
            dp[i] = (min(prev_min*nums[i], nums[i]), max(prev_max*nums[i], nums[i]))
            ans = max(ans , max(prev_max*nums[i], nums[i]))
        
        return ans
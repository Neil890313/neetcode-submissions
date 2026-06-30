class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:
            return False
        half = total//2
        # dp[i] 是指 用目前 nums 中的數字，能否湊出一些並組合出數字 i
        dp = [False]*(half+1)
        # base case
        dp[0] = True
        # [重點] 0/1 背包問題
        # 與之前湊目標的題目相反，因為工具箱中的工具只能使用一次，因此放在外迴圈
        # 一個一個把數字納入考慮,每個數字只輪到一次
        for num in nums:
            # Q2:為什麼內層要倒著走?
            # 因為「外層跑數字」只擋住了『跨輪重複』,還沒擋住『同一輪內重複』。倒著走補上這個漏洞。
            for i in range(half, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        return dp[half]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > lowest:
                ans = max(ans, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return ans
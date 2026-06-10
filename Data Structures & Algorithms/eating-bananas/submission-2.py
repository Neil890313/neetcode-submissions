class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 首先需要找出最慢(L)以及最快(R)的區間
        l = 1
        r = max(piles)
        # Answer(min)
        ans = r

        while l <= r:
            mid = (l+r)//2

            # 計算時間，需要花多少小時
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                # 太慢了
                l = mid + 1
        return ans
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float('inf')

        while l <= r:
            mid = (l+r)//2
            hours = 0
            for p in piles:
                a, b = divmod(p, mid)
                if b != 0:
                    a += 1
                hours += a
            if hours <= h:
                ans = min(ans, mid)
                r = mid -1
            else:
                l = mid +1
        return ans


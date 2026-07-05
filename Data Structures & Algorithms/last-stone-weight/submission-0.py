class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x*(-1) for x in stones]
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            remain = a-b
            if remain > 0:
                heapq.heappush(stones, -remain)
        return 0 if not stones else -stones[0]
            


        

        
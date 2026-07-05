from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(node):
            return sqrt((0 - node[0])**2 + (0 - node[1])**2)
        
        heap = []
        for i in points:
            heap.append((-getDistance(i), i))

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        ans = []
        for distance, node in heap:
            ans.append(node)
        return ans

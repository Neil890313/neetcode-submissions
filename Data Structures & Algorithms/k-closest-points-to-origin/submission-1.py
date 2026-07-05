from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(node):
            return sqrt((0 - node[0])**2 + (0 - node[1])**2)
        
        # heap = []
        # for i in points:
        #     heap.append((-getDistance(i), i))

        # heapq.heapify(heap)

        # while len(heap) > k:
        #     heapq.heappop(heap)

        heap = []
        for p in points:
            dist = getDistance(p)
            
            # 💎 技巧二：動態大逃殺（VIP包廂永遠維持在 K 的大小）
            # 如果包廂還沒滿，無條件直接進去
            if len(heap) < k:
                # 依然使用負數，因為我們要找「最近」的 K 個，所以要淘汰「最遠（值最大）」的人
                # 負數之後，最遠的人（如 -25）會浮在 Min-Heap 的最上面
                heapq.heappush(heap, (-dist, p))
            else:
                # 包廂滿了！新來的挑戰者如果比包廂裡「最遠的那個人」還要近（因為是負數，所以是 -dist > heap[0][0]）
                if -dist > heap[0][0]:
                    heapq.heappop(heap)          # 踢走目前包廂裡最遠的肉腳
                    heapq.heappush(heap, (-dist, p)) # 迎來更近的強者
        
        return [node for distance, node in heap]

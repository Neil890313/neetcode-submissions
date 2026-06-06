class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # quese 內部存放的為 index
        q = deque()
        ans = []

        for r in range(len(nums)):
            # step1: 排除所有比新一筆元素小的所有元素後，加入新值，實現大到小排序
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # step2: 檢查最大值是否過期
            if q[0] < r-k+1:
                q.popleft()
            # step3: 當 r 比 k 大時，開始紀錄所有 window 中的最大值(q[0])
            if r >= k-1:
                ans.append(nums[q[0]])
        return ans 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            # check 老大過期沒
            if q[0] < i-k+1:
                q.popleft()
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans
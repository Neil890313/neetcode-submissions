class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tmp = collections.deque(nums[:k])
        ans = []
        ans.append(max(tmp))

        for r in range(k, len(nums)):
            tmp.popleft()
            tmp.append(nums[r])
            ans.append(max(tmp))
        return ans
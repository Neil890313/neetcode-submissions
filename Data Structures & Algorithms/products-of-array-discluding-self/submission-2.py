class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)

        # left 
        now = 1
        for i in range(1, len(nums)):
            now = now*nums[i-1]
            left[i] = now
        
        # right
        now = 1
        for i in range(len(nums)-2, -1, -1):
            now = now*nums[i+1]
            right[i] = now

        # total
        ans = []

        for i, j in zip(left, right):
            ans.append(i*j)

        return ans

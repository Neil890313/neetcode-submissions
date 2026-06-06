class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)

        # left pre-sum
        left_product = 1
        for i in range(1, len(nums)):
            left_product = left_product*nums[i-1]
            left[i] = left_product

        # right pre-sum
        right_product = 1
        for i in range(len(nums)-2, -1, -1):
            right_product = right_product*nums[i+1]
            right[i] = right_product
        
        # total
        ans = []
        for l, r in zip(left, right):
            ans.append(l*r)
        
        return ans
        

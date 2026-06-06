class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict = {}
        
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in check_dict:
                return [check_dict.get(tar), i]
            check_dict[nums[i]] = i

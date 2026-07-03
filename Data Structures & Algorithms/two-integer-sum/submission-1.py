class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict = {}

        for i in range(len(nums)):
            now = target-nums[i]
            if now in check_dict:
                return [check_dict[now], i]
            else:
                check_dict[nums[i]] = i


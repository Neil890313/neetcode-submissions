class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        now_set = set()

        for i in range(len(nums)):
            if nums[i] - 1 in nums:
                length = 1
                while nums[i] - length in nums:
                    length += 1
                longest = max(longest, length)
        return 0 if not nums else longest
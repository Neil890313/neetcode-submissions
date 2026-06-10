class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        for i in nums:
            if i - 1 in nums:
                length = 1
                while i - length in nums:
                    length += 1
                count = max(count, length)
        return count
        
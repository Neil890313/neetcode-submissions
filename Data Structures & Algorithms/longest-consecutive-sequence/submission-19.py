class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1

        for i in nums:
            if i-1 in nums:
                length = 1
                while i-length in nums:
                    length += 1
                longest = max(longest, length)
        return longest

        
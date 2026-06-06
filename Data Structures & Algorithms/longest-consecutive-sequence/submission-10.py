class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check_set = set(nums)

        count = 1
        for i in nums:
            j = i
            if j - 1 in check_set:
                length = 1
                while j - length in check_set:
                    length += 1
                count = max(count, length)
        return count
        
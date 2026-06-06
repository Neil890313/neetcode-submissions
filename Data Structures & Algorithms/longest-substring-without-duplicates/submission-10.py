class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        tmp_set = set()

        for r in range(len(s)):
            while s[r] in tmp_set:
                tmp_set.remove(s[l])
                l += 1
            tmp_set.add(s[r])
            longest = max(longest, len(tmp_set))

        return longest
            
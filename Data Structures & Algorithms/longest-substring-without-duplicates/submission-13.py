class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = 0
        ans = 0

        for i in range(len(s)):
            while subset and s[i] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[i])
            ans = max(ans, len(subset))
        return ans
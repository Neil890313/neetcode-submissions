class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in tmp:
                tmp.remove(s[l])
                l += 1
            
            tmp.add(s[r])
            
            longest = max(longest, r - l + 1)
            
        return longest
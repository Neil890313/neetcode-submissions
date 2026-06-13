class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        check = deque()

        for r in range(len(s)):
            while s[r] in check:
                check.popleft()
                l += 1
            check.append(s[r])
            ans = max(ans, r-l+1)
        return ans
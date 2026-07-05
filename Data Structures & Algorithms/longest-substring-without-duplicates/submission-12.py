class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subarray = deque()
        ans = 0

        for i in range(len(s)):
            while subarray and s[i] in subarray:
                subarray.popleft()
            subarray.append(s[i])
            ans = max(ans, len(subarray))
        return ans
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tmp_dict = collections.defaultdict(int)

        l = 0
        longest = 0
        freq = 0

        for r in range(len(s)):
            tmp_dict[s[r]] += 1
            freq = max(freq, tmp_dict[s[r]])
            while r-l+1 - freq > k:
                tmp_dict[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)

        return longest
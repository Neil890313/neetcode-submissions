class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check_dict = collections.defaultdict(int)
        longest, l, max_freq = 0, 0, 0

        for r in range(len(s)):
            check_dict[s[r]] += 1
            max_freq = max(max_freq, check_dict[s[r]])

            while (r-l+1) -max_freq > k:
                check_dict[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
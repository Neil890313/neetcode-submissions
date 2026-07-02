class Solution:
    def longestPalindrome(self, s: str) -> str:

        def splash(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        res = ""

        for i in range(len(s)):
            # 單
            odd_str = splash(i, i)
            if len(odd_str) > len(res):
                res = odd_str
            # 雙
            even_str = splash(i-1, i)
            if len(even_str) > len(res):
                res = even_str
        return res
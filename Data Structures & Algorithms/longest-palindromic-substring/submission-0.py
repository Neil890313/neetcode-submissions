class Solution:
    def longestPalindrome(self, s: str) -> str:
        # center expend 
        res = ""

        # helper function - expend
        def expend(l, r):
            # 終止條件
            # 1. 左右其中一邊碰壁
            # 2. 左右不同
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # 跳出迴圈，表示目前這個迴圈失敗，答案是前一個
            return s[l+1:r]
        
        for i in range(len(s)):
            # 兩種情況
            # 奇數
            odd_str = expend(i, i)
            # 偶數
            even_str = expend(i-1, i)

            if len(odd_str) > len(res):
                res = odd_str
            if len(even_str) > len(res):
                res = even_str
        return res
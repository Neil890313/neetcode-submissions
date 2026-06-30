class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0

        def expend(l, r):
            count = 1
            # 終止條件
            # 左右其中之一碰牆
            # 左右不同
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count-1
        for i in range(len(s)):
            # 兩種情況
            # 奇數
            total_count += expend(i,i)
            # 偶數
            total_count += expend(i-1, i)
        return total_count
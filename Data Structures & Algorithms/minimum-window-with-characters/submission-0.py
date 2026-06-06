class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        min_length = float('inf')
        min_start = 0
        need_dict = collections.Counter(t)
        now_dict = collections.defaultdict(int)
        already_num = 0

        for r in range(len(s)):
            if s[r] in need_dict:
                now_dict[s[r]] += 1
                # 如果還沒湊滿，則以達成值 already_num + 1
                if need_dict[s[r]] >= now_dict[s[r]]:
                    already_num += 1
            # 如過需要的字母都湊滿了，則可以開始
            # 1. 紀錄長度，以及由於這一題要return 最短字串，所以要紀錄最短字串的 start 
            # 2. 縮 L
            while already_num == len(t):
                # step1
                if min_length > r-l+1:
                    min_length = r-l+1
                    min_start = l
                # step2
                if s[l] in need_dict:
                    now_dict[s[l]] -= 1
                    # value is 0
                    if now_dict[s[l]] < need_dict[s[l]]:
                        already_num -= 1
                l += 1
        return "" if min_length == float('inf') else s[min_start : min_start + min_length]
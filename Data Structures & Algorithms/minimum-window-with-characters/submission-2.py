class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = Counter(t)
        now_dict = defaultdict(int)
        min_length = float('inf')
        min_start = 0
        already_len = 0
        l = 0

        for r in range(len(s)):
            if s[r] in need_dict:
                now_dict[s[r]] += 1
                if now_dict[s[r]] <= need_dict[s[r]]:
                    already_len += 1
            while already_len == len(t):
                if r-l+1 < min_length:
                    min_length = r-l+1
                    min_start = l
                if s[l] in need_dict:
                    now_dict[s[l]] -= 1
                    if  now_dict[s[l]] < need_dict[s[l]]:
                        already_len -= 1
                l += 1
        return "" if min_length == float('inf') else s[min_start:min_start+min_length]
                 
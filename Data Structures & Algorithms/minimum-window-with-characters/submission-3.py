class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 需要的字母
        need_dict = Counter(t)
        # 收集的字母及數量
        collect_dict = defaultdict(int)
        collect_num = 0
        # 紀錄最短
        min_len = float('inf')
        min_start = 0

        l = 0

        for r in range(len(s)):
            if s[r] in need_dict:
                collect_dict[s[r]] += 1
                if collect_dict[s[r]] <= need_dict[s[r]]:
                    collect_num += 1
            while collect_num == len(t):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_start = l
                if s[l] in need_dict:
                    collect_dict[s[l]] -= 1
                    if collect_dict[s[l]] < need_dict[s[l]]:
                        collect_num -= 1
                l += 1
        return '' if min_len == float('inf') else s[min_start: min_start+min_len]
                 
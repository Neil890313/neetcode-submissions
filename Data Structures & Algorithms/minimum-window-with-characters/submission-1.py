class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        need_dict = collections.Counter(t)
        # 確認目前收集情況
        collect_dict = collections.defaultdict(int)
        already_num = 0
        # 確認最短的長度以及開始處
        min_length = float('inf')
        min_start = 0


        for r in range(len(s)):
            # 如果 s[r] 為需要的字母
            if s[r] in need_dict:
                collect_dict[s[r]] += 1
                # 如果還未收集完畢或是剛好收集完，則 already_num +1
                if collect_dict[s[r]] <= need_dict[s[r]]:
                    already_num += 1
            # 如果收集完畢 
            while already_num == len(t):
                # 抓最小值，以及紀錄開頭 L
                if r-l+1 < min_length:
                    min_length = r-l+1
                    min_start = l
                if s[l] in need_dict:
                    collect_dict[s[l]] -= 1
                    if collect_dict[s[l]] < need_dict[s[l]]:
                        already_num -= 1
                l += 1
        return '' if min_length == float('inf') else s[min_start: min_start+min_length]
                
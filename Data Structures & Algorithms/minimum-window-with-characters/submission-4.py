class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        min_start = None

        check_dict = Counter(t)
        collected_dict = defaultdict(int)
        already_num = 0
        l = 0

        for r in range(len(s)):
            if s[r] in check_dict:
                collected_dict[s[r]] += 1
                if collected_dict[s[r]] <= check_dict[s[r]]:
                    already_num += 1
            while already_num == len(t):
                if r-l+1 < min_length:
                    min_length = r-l+1
                    min_start = l
                left_node = s[l]
                if left_node in check_dict:
                    collected_dict[left_node] -= 1
                    if collected_dict[left_node] < check_dict[left_node]:
                        already_num -= 1
                l += 1
        return "" if min_length == float('inf') else s[min_start:min_start + min_length]
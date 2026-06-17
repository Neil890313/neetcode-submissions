class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_dict = Counter(s1)
        now_dict = {}
        l = 0

        for r in range(len(s2)):
            now_dict[s2[r]] = now_dict.get(s2[r], 0) + 1
            
            if r > len(s1)-1:
                now_dict[s2[l]] -= 1
                if now_dict[s2[l]] == 0:
                    del now_dict[s2[l]]
                l += 1
            if now_dict == check_dict:
                return True
        return False
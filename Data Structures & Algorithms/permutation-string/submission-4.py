class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l = 0
        # r = len(s1) -1

        # for r in range((len(s1) -1), len(s2)):
        #     if sorted(s2[l:r+1]) == sorted(s1):
        #         return True
        #     else:
        #         l += 1
        # return False
        check_dict = Counter(s1)
        now_dict = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            now_dict[s2[r]] += 1
            if r >= len(s1):
                now_dict[s2[l]] -= 1
                if now_dict[s2[l]] == 0:
                    del now_dict[s2[l]]
                l += 1
            if check_dict == now_dict:
                return True
        return False
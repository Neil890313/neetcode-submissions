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
        check_dict = collections.Counter(s1)
        collect_dict = collections.defaultdict(int)

        for r in range(len(s2)):
            collect_dict[s2[r]] += 1

            if r >= len(s1):
                left_char = s2[r-len(s1)]
                collect_dict[left_char] -= 1
                if collect_dict[left_char] == 0:
                    del collect_dict[left_char]
            if check_dict == collect_dict:
                return True
        return False
            
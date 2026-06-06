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
        tmp_dict = collections.Counter()

        # 因為是固定 length 的 window，不需要宣告 L
        for i in range(len(s2)):
            tmp_dict[s2[i]] += 1

            # 如果超過 len(s1) 的長度後，每一次都需要移除最左邊的 elements
            if i >= len(s1):
                left_char = s2[i-len(s1)]
                tmp_dict[left_char] -= 1
                # 最大的重點，如果 dict 中值為0，必須移除，以免影響後續的判斷
                if tmp_dict[left_char] == 0:
                    del tmp_dict[left_char]
            if check_dict == tmp_dict:
                return True
        return False
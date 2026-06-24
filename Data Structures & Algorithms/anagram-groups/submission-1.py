class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_dict = defaultdict(list)

        for i in strs:
            sorted_i = "".join(sorted(i))
            check_dict[sorted_i].append(i)
        
        ans = []
        for value in check_dict.values():
            ans.append(value)

        return ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_dict = collections.defaultdict(list)

        for i in strs:
            s = "".join(sorted(i))
            check_dict[s].append(i)
        return [i for i in check_dict.values()]
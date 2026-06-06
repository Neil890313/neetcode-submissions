class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check_dict = collections.Counter(nums)

        # bucket sort
        freq = [[] for _ in range(len(nums)+1)]
        for key, value in check_dict.items():
            freq[value].append(key)
        res = []

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
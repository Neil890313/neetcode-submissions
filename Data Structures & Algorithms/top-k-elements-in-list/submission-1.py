class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for i in nums:
            count_dict[i] += 1
        bucket = [[] for _ in range(len(nums)+1)]

        for key, value in count_dict.items():
            bucket[value].append(key)

        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if not bucket[i]:
                continue
            else:
                for j in bucket[i]:
                    if k != 0:
                        ans.append(j)
                        k -= 1
        return ans
        
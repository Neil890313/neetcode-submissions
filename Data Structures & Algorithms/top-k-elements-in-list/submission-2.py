class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        check_dict = Counter(nums)

        # build bucket list
        bucket_list = defaultdict(list)

        for key, value in check_dict.items():
            bucket_list[value].append(key)

        ans = []
        for i in range(len(nums), -1, -1):
            for j in range(len(bucket_list[i])):
                if k != 0:
                    ans.append(bucket_list[i][j])
                    k -= 1
        return ans
        
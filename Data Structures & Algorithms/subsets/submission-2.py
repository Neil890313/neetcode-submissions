class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrace(start):
            # 收集 path
            res.append(path[:])

            for i in range(start, len(nums)):
                # 加入選項
                path.append(nums[i])
                # dfs
                backtrace(i+1)
                # 撤銷選項
                path.pop()

        backtrace(0)
        return res